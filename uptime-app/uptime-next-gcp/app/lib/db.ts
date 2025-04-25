// app/lib/db.ts

import { Client, QueryResult, QueryResultRow } from "pg";
import { loadEnvConfig } from "@next/env";

const projectDir = process.cwd();
loadEnvConfig(projectDir);

// Generate a Postgres client
export async function getClient(): Promise<Client> {
  if (process.env.DB_URL) {
    return new Client({
      connectionString: process.env.DB_URL,
    });
  }

  return new Client({
    user: process.env.DB_USER,
    host: process.env.DB_HOST,
    database: process.env.DB_NAME,
    password: process.env.DB_PASS,
    port: parseInt(process.env.DB_PORT ?? "5432"),
  });
}

// Typed SQL query function
export async function sql<T extends QueryResultRow = QueryResultRow>(
  sql: string,
  values?: unknown[]
): Promise<QueryResult<T>> {
  const client = await getClient();
  await client.connect();

  try {
    const res = await client.query<T>(sql, values);
    return res;
  } finally {
    await client.end();
  }
}
