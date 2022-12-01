

HeightToCm = lambda feet, inches: round(feet*30.48 + inches*2.54,2)
    
PoundToKilogram = lambda lbs: round(lbs*0.453592,3)

Male_BMR =  lambda weight_lb, height_ft_in, age: round(88.362 + (13.397 * PoundToKilogram(weight_lb)) + (4.799 * HeightToCm(height_ft_in[0],height_ft_in[1])) - (5.677 * age),0)

Female_BMR =  lambda weight_lb, height_ft_in, age: round(447.593 + (9.247 * PoundToKilogram(weight_lb)) + (3.098 * HeightToCm(height_ft_in[0],height_ft_in[1])) - (4.330 * age),0)

# estimated number of calories a person with a given BMR and activity level needs to maintain their weight
AMR = lambda BMR, activity_level: round(BMR * activity_level)