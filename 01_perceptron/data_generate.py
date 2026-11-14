import random
import csv
import argparse

def generate_perceptron_data(n_rows, filename="placement.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['cgpa', 'resume_score', 'placed'])
        
        for _ in range(n_rows):
            # Generate values
            cgpa = round(random.uniform(0, 10), 2)
            resume_score = round(random.uniform(0, 100), 2)
            
            # Real-world logic calculation:
            # resume_score/10 scales the 0-100 score down to a 0-10 scale for the math
            # 60% weight to CGPA, 40% weight to Resume
            base_score = (0.6 * cgpa) + (0.4 * (resume_score / 10))
            
            # Real-world unpredictability (e.g., a bad interview day, or getting lucky)
            luck_factor = random.uniform(-1.0, 1.0)
            final_score = base_score + luck_factor
            
            # If the student's final score passes the cutoff of 6.0 out of 10, they are placed
            if final_score >= 6.0:
                placed = 1
            else:
                placed = 0
                
            writer.writerow([cgpa, resume_score, placed])
            
    print(f"Successfully generated {n_rows} rows in '{filename}'")
    print("Scenario: High CGPA and High Resume strictly approach Placed (1).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic placement data for a perceptron.")
    parser.add_argument(
        "N", 
        type=int, 
        nargs="?", 
        default=1000, 
        help="Number of rows to generate (default: 1000)"
    )
    
    args = parser.parse_args()
    
    generate_perceptron_data(args.N)
