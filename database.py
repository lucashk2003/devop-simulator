# database.py
import sqlite3
from config import DATABASE_PATH
import json
from datetime import datetime

def get_conn():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS simulations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            params TEXT,
            results TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_simulation(params, results):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO simulations (timestamp, params, results)
        VALUES (?, ?, ?)
    ''', (datetime.now().isoformat(), json.dumps(params), json.dumps(results)))
    sim_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return sim_id

def get_simulations():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, timestamp, params FROM simulations ORDER BY timestamp DESC LIMIT 20')
    rows = cur.fetchall()
    conn.close()
    return rows

def get_simulation_by_id(sim_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM simulations WHERE id = ?', (sim_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return {
            'id': row['id'],
            'timestamp': row['timestamp'],
            'params': json.loads(row['params']),
            'results': json.loads(row['results'])
        }
    return None