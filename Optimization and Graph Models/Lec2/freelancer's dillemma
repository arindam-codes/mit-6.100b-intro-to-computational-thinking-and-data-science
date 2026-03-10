

class Project():
    
    def __init__(self, name, hour, fee):
        self.name = name
        self.hour = hour
        self.fee = fee
        
    def get_name(self):
        return self.name
    
    def get_hour(self):
        return self.hour
    
    def get_fee(self):
        return self.fee
    
def project_modeler(name, hour, fee):
    
    projects = []
    for i in range(len(name)):
        project = Project(name[i], hour[i], fee[i])
        projects.append(project)
        
    return projects

 

def greedy(projects, max_function):
    
    available_hours = 0
    # case 1 keeping the job
    total_hours = 40
    profitable_projects = []
    
    sorted_projects = sorted(projects, key=max_function, reverse=True)
    
    for project in sorted_projects:
        
        if project.get_hour() + available_hours <= total_hours:
            profitable_projects.append(project)
            available_hours += project.get_hour()
            
    return profitable_projects
            
            
projects_list = [
    ("Logo Design", 10, 200),
    ("Website Development", 25, 600),
    ("Brochure Design", 8, 100),
    ("Mobile App Prototype", 30, 900),
    ("Social Media Campaign", 5, 60),
    ("Illustration", 12, 250),
    ("Copywriting", 6, 80),
    ("Video Editing", 20, 400),
    ("Photography Session", 15, 300),
    ("Consultation", 4, 50),
    ("UX Audit", 7, 120),
    ("Animation", 18, 500),
    ("SEO Optimization", 9, 150),
    ("E-commerce Setup", 22, 700),
    ("Newsletter Design", 3, 40)
]
            
name = [name[0] for name in projects_list]  
hour = [hour[1] for hour in projects_list]  
fee = [fee[2] for fee in projects_list]  

projects = project_modeler(name, hour, fee)
    
    
def greedy_printer(greedy):
    
    result = greedy
    
    fee = 0
    for project in result:
        
        fee += project.get_fee()
        print(project.get_name(), " fee: $", project.get_fee(), project.get_hour(),"hrs")
    print("Total Fee: ", fee,"\n")


greedy_printer(greedy(projects, lambda project: project.get_fee()))
greedy_printer(greedy(projects, lambda project: 1 / project.get_hour()))
greedy_printer(greedy(projects, lambda project: project.get_fee() / project.get_hour()))
