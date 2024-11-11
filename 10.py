def calculate_weighted_average(grades, weights, subjects): 
    if len(grades) != len(weights) or len(grades) != len(subjects): 
        raise ValueError("") 
     
    total_weighted_sum = sum(g * w for g, w in zip(grades, weights)) 
    total_weights = sum(weights) 
     
    weighted_average = total_weighted_sum / total_weights 
     
    for subject, grade, weight in zip(subjects, grades, weights): 
        print(f"Subject: {subject}, Grade: {grade}, Weight: {weight}") 
         
    return weighted_average 

subjects = ["History","Literature", "Geography", "Programming","Math", "Science"]
grades = [18, 15, 20, 17, 17, 19] 
weights = [2, 3, 1, 4, 3, 2]  

average = calculate_weighted_average(grades, weights, subjects) 
print(f" {average}")
