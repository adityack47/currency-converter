💰 AI-Based Currency Converter
A simple currency converter that fetches real-time exchange rates and converts between different currencies. Uses NumPy for calculations and the Exchange Rate API for live data.

📌 Features
✔️ Fetches live exchange rates from an API.
✔️ Converts any currency to another.
✔️ Uses NumPy for efficient calculations.
✔️ Beginner-friendly but practical.

🚀 Installation & Usage
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/YOUR-USERNAME/currency-converter.git
cd currency-converter
2️⃣ Install Dependencies
bash
Copy
Edit
pip install numpy requests
3️⃣ Run the Script
bash
Copy
Edit
python currency_converter.py
4️⃣ Enter amount & currency codes when prompted
📊 Example Output
java
Copy
Edit
Available Currencies: ['USD', 'EUR', 'INR', 'GBP', 'JPY', ...]
Enter amount: 100
Enter the currency you have (e.g., USD, EUR, INR): USD
Enter the currency you want (e.g., USD, EUR, INR): INR
100 USD = 8300.50 INR
📂 Project Structure
bash
Copy
Edit
/currency-converter
│── currency_converter.py  # Main Python script
│── README.md              # Project documentation
🔗 API Used
ExchangeRate-API
