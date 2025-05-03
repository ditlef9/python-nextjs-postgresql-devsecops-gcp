// app/(public)/public-migrations/api-run-migrations/route.ts

import { sql } from "@/app/lib/db";
import { NextResponse } from "next/server";
import { promises as fs } from "fs";
import path from "path";

export async function GET(request: Request) {

  // Check if the environment is 'development' and the directory ends with '.development'
  const env = process.env.NODE_ENV;

  // 1. Create the migrations table if it does not exist
  await sql(`
    CREATE TABLE IF NOT EXISTS u_migrations (
      migration_id SERIAL PRIMARY KEY,
      migration_module VARCHAR(255),
      migration_name VARCHAR(255) NOT NULL,
      migration_run_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
  `);
  await sql(`
    SELECT setval(pg_get_serial_sequence('u_migrations', 'migration_id'), coalesce(max(migration_id)+1, 1), false) FROM u_migrations;
  `);

  
  // Initialize counters
  let migrationsRun = 0;
  let migrationsSkipped = 0;
  let migrationErrors: { file: string; error: string }[] = [];

  // 2. Loop through all directories in "@/migrations" and save them to a variable
  const migrationsPath = path.join(process.cwd(), "migrations");
  const migrationsDirectories = await fs.readdir(migrationsPath, { withFileTypes: true });

  // 3. Loop through migrationsDirectories and only process those ending with '.development'
  for (const directory of migrationsDirectories) {
    if (directory.isDirectory()) {
      const modulePath = path.join(migrationsPath, directory.name);
      const migrationFiles = await fs.readdir(modulePath);

      for (const file of migrationFiles) {
        // Check if the file exists in the database table 
        const res = await sql(
          "SELECT migration_id, migration_module, migration_name, migration_run_timestamp FROM u_migrations WHERE migration_module=$1 AND migration_name=$2",
          [directory.name, file]
        );

        if (res.rows.length === 0) {
          // Run the file contents of the migration file
          console.log(`app/(public)/public-migrations/api-run-migrations/route.ts::=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-`);
          console.log(`app/(public)/public-migrations/api-run-migrations/route.ts::Migration ${directory.name}/${file} Start`);

          const filePath = path.join(modulePath, file);
          const fileContents = await fs.readFile(filePath, "utf-8");

          try {
            // Execute the migration SQL
            if (directory.name.endsWith('.development')) {
              // Only run if in development environment
              if (env === "development") {
                await sql(fileContents);
              }
            } else {
              // Run for all other directories
              await sql(fileContents);
            }

            // Insert record into migrations after successful execution
            await sql(
              "INSERT INTO u_migrations (migration_module, migration_name) VALUES ($1, $2)",
              [directory.name, file]
            );

            console.log(`app/(public)/public-migrations/api-run-migrations/route.ts::Migration ${directory.name}/${file} Success!`);
            migrationsRun++;
          } catch (error) {
            console.error(`app/(public)/public-migrations/api-run-migrations/route.ts::Error ${directory.name}/${file}:`, error);

            // Handle 'unknown' type for error
            let errorMessage = "Unknown error";
            if (error instanceof Error) {
              errorMessage = error.message;
            }

            migrationErrors.push({ file, error: errorMessage });
          }
          console.log(`app/(public)/public-migrations/api-run-migrations/route.ts::=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-`);
        } else {
          migrationsSkipped++;
        }
      }
    }
  }

  // 6. Return the result
  return NextResponse.json({
    "message": `${migrationsRun} migrations run`,
    "data": "",
    "error": migrationErrors,
  });
}
