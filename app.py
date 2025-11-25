# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, save_simulation, get_simulations, get_simulation_by_id
from simulator import run_devops_simulation
import os

app = Flask(__name__)
app.secret_key = 'devops2025'

# Crear carpeta data si no existe
os.makedirs('data', exist_ok=True)

@app.route('/')
def index():
    simulations = get_simulations()
    return render_template('index.html', simulations=simulations)

@app.route('/simulate', methods=['POST'])
def simulate():
    try:
        params = {
            'num_developers': int(request.form['developers']),
            'num_testers': int(request.form['testers']),
            'sprint_days': int(request.form['sprint_days']),
            'automation_level': int(request.form['automation']) / 100,
            'bug_probability': int(request.form['bugs']) / 100,
            'num_sprints': int(request.form['sprints']),
            'tasks_per_sprint': int(request.form['tasks_per_sprint'])
        }
        
        batch_size = int(request.form.get('batch_size', 1))
        if batch_size < 1:
            batch_size = 1
        if batch_size > 20000:
            flash("Máximo 20.000 corridas por ejecución")
            batch_size = 20000

        all_results = []
        for _ in range(batch_size):
            result = run_devops_simulation(params)
            all_results.append(result)

        # === Estadísticas agregadas ===
        import numpy as np
        lead_times = [r['lead_time_avg'] for r in all_results]
        defect_rates = [r['defect_rate'] for r in all_results]
        deploy_rates = [r['deploy_success_rate'] for r in all_results]

        summary = {
            'batch_size': batch_size,
            'lead_time': {
                'mean': round(np.mean(lead_times), 2),
                'std': round(np.std(lead_times), 2),
                'p95': round(np.percentile(lead_times, 95), 2),
                'min': round(min(lead_times), 2),
                'max': round(max(lead_times), 2)
            },
            'defect_rate': {
                'mean': round(np.mean(defect_rates), 2),
                'std': round(np.std(defect_rates), 2)
            },
            'deploy_success_rate': {
                'mean': round(np.mean(deploy_rates), 2),
                'std': round(np.std(deploy_rates), 2)
            }
        }
        if batch_size == 1:
            # Guardamos también los datos por sprint para compatibilidad con gráficos
            summary['sprint_data'] = all_results[0]['sprint_data']
        
        sim_id = save_simulation(params, summary, batch_size)
        return redirect(url_for('results', sim_id=sim_id))

    except Exception as e:
        flash(f"Error: {e}")
        return redirect('/')

@app.route('/results/<int:sim_id>')
def results(sim_id):
    sim = get_simulation_by_id(sim_id)
    if not sim:
        flash("Simulación no encontrada")
        return redirect('/')
    return render_template('results.html', sim=sim)

@app.route('/history')
def history():
    simulations = get_simulations()
    return render_template('history.html', simulations=simulations)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True, use_reloader=False)
    #app.run()
    #app.run(debug=True, use_reloader=False, threaded=True)
    #import threading
    #threading.Thread(target=app.run, kwargs={'debug': True, 'use_reloader': False}).start()