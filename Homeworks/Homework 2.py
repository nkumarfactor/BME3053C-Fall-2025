bp_readings = [120, 137, 151, 123, 162, 173, 127, 154]
x = min(bp_readings)
y = max(bp_readings)
def normalize_readings(values):
  min_value = min(values)
  max_value = max(values) 
  
  normalized_values = []

  for x in values: 
    norm_x = (x - min_value)/(max_value - min_value)
    normalized_values.append(norm_x)
  return normalized_values 

normalized_bp = normalize_readings(bp_readings)
print("Original readings:", bp_readings)
print("Normalized readings:", normalized_bp) 
