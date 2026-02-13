from django.shortcuts import render
from .ml.predictor import prediction

def predict_car_price(request):
    context = {}
    
    if request.method == 'POST':
        try:
            year = int(request.POST.get('year'))
            km_driven = int(request.POST.get('km_driven'))
            car_model = request.POST.get('car_model')

            
            if km_driven > 80000:
                driven_factor = km_driven * 1.2
            elif km_driven > 50000:
                driven_factor = km_driven * 0.9
            elif km_driven > 40000:
                driven_factor = km_driven * 0.7
            elif km_driven > 20000:
                driven_factor = (km_driven * 0.4)
            else:
                driven_factor = (km_driven * 0.2)
            
            brand_values = {
            'alto': 0.55,    
            'i10': 0.55,
            'kwid': 0.55,
            'swift': 0.75,
            'i20': 0.75,
            'baleno': 0.75,
            'city': 0.9,
            'verna': 0.9,
            'creta': 0.9,
            'octavia': 1.3,
            'superb': 1.3,
            'fortuner': 1.3,
            }
        
            brand_value = brand_values.get(car_model, 0.30)
      
            predicted_price = prediction(year, km_driven)
            
            age = 2025 - year
            if age > 10:  
                true_value = (predicted_price * 0.5 * brand_value) - (driven_factor * 100)
            else:
                true_value = (predicted_price * brand_value) - (driven_factor * 50)

            true_value = max(true_value, predicted_price * 0.1)  
            
            context['predicted_price'] = f"₹{true_value:,.2f}"
            
        except (ValueError, TypeError):
            context['error'] = "Invalid input values"
    
    return render(request, 'home.html', context)

