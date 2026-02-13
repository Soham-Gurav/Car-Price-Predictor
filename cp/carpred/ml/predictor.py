import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('D:\CP\cp\carpred\data\car_inprogress.csv')
df['engine'] = df['engine'].str.replace('CC', '', case=False).str.strip().astype(float)
df = df.dropna(subset=['selling_price', 'year', 'km_driven'])

X = df[['year', 'km_driven']]
y = df['selling_price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)


def prediction(input_year, input_km_driven):
    predicted_price = model.predict([[input_year, input_km_driven]])[0]
    return round(predicted_price, 2)

