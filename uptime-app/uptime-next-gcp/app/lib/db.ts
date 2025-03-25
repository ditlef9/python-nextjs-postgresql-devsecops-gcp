// app/lib/db.ts

import { Client, QueryResult } from "pg";
import { loadEnvConfig } from "@next/env";

const projectDir = process.cwd();
loadEnvConfig(projectDir)

// Generate a Postgres client
export async function getClient(): Promise<Client>{
    // console.log("db.ts::getClient()::Init");

    // Client with URL
    if (process.env.DB_URL) {
        // console.log("db.ts::getClient()::Connecting client with URL"); //  + "?sslmode=require"
        const client = new Client({
          connectionString: process.env.DB_URL,
        });
        // console.log("db.ts::getClient()::Connecting client with URL [connected]");
        return client;
    }

    // Client with username, host, database, password
    // console.log("db.ts::getClient()::Connecting client with username, host, database, password");
    const client = new Client({
        user: process.env.DB_USER,
        host: process.env.DB_HOST,
        database: process.env.DB_NAME,
        password: process.env.DB_PASS,
        port: parseInt(process.env.DB_PORT!)
    });
    // console.log("db.ts::getClient()::Connecting client with username, host, database, password [connected]");
    return client;
}

// Handle connection, SQL and end the connection
export async function sql(sql: string, values?: Array<any>): Promise<QueryResult<any>> {
    // console.log("db.ts::sql()::Querying");
    const client = await getClient();
    await client.connect();
    // console.log("db.ts::sql()::Querying Connect");
    const res = await client.query(sql, values);
    // console.log("db.ts::sql()::Querying Await client query");
    await client.end();
    // console.log("db.ts::sql()::Querying [OK]");
    return res;
}