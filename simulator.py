# simulator.py
import random
import numpy as np

def run_devops_simulation(params):
    devs = params['num_developers']
    testers = params['num_testers']
    sprint_days = params['sprint_days']
    automation = params['automation_level']
    bug_prob = params['bug_probability']
    num_sprints = params['num_sprints']
    tasks_per_sprint = params['tasks_per_sprint']
    
    # Métricas acumuladas
    total_lead_time = []
    defects_per_sprint = []
    successful_deploys = []
    tasks_completed = []
    
    for sprint in range(num_sprints):
        tasks_in_sprint = tasks_per_sprint
        completed = 0
        defects = 0
        lead_times = []
        
        for _ in range(tasks_in_sprint):
            # Monte Carlo: tiempo de desarrollo
            dev_time = random.uniform(1, 5) / devs
            
            # Posibilidad de bug
            has_bug = random.random() < bug_prob
            if has_bug:
                defects += 1
                dev_time += random.uniform(1, 3)  # rework
            
            # Testing (más rápido si hay automatización)
            test_time = random.uniform(0.5, 2) * (1 - automation * 0.8)
            if testers > 0:
                test_time /= testers
            
            # Deploy (probabilidad de éxito depende de automatización)
            deploy_success = random.random() < (0.6 + automation * 0.4)
            
            total_time = dev_time + test_time
            if deploy_success:
                completed += 1
                lead_times.append(total_time)
        
        total_lead_time.append(np.mean(lead_times) if lead_times else 0)
        defects_per_sprint.append(defects)
        successful_deploys.append(completed)
        tasks_completed.append(completed)
    
    return {
        'lead_time_avg': round(np.mean(total_lead_time), 2),
        'defect_rate': round(np.mean(defects_per_sprint) / tasks_per_sprint * 100, 1),
        'deploy_success_rate': round(np.mean(successful_deploys) / tasks_per_sprint * 100, 1),
        'sprint_data': {
            'lead_times': total_lead_time,
            'defects': defects_per_sprint,
            'deploys': successful_deploys
        }
    }