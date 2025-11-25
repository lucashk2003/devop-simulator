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
            batch_size INTEGER DEFAULT 1,
            results_summary TEXT
        )
    ''')
    # Migración automática para quienes ya tenían la DB vieja
    try:
        conn.execute("ALTER TABLE simulations ADD COLUMN batch_size INTEGER DEFAULT 1")
    except sqlite3.OperationalError:
        pass
    try:
        conn.execute("ALTER TABLE simulations ADD COLUMN results_summary TEXT")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()

def save_simulation(params, results_summary, batch_size=1):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO simulations (timestamp, params, batch_size, results_summary)
        VALUES (?, ?, ?, ?)
    ''', (datetime.now().isoformat(), json.dumps(params), batch_size, json.dumps(results_summary)))
    sim_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return sim_id

def get_simulations():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT id, timestamp, params, batch_size FROM simulations ORDER BY timestamp DESC LIMIT 30')
    rows = cur.fetchall()
    conn.close()
    simulations = []
    for row in rows:
        sim = dict(row)
        sim['params'] = json.loads(sim['params'])
        simulations.append(sim)
    return simulations

def get_simulation_by_id(sim_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM simulations WHERE id = ?', (sim_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        sim = dict(row)
        sim['params'] = json.loads(sim['params'])
        sim['results_summary'] = json.loads(sim['results_summary'])
        return sim
    return None