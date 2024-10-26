# Define tax data for each year
tax_data = {
    2005: {'personal_allowance': 0, 'basic_rate': 10, 'basic_threshold': 2090, 'higher_rate': 22, 'additional_rate': 40, 'additional_threshold': 32400},
    2006: {'personal_allowance': 0, 'basic_rate': 10, 'basic_threshold': 2150, 'higher_rate': 22, 'additional_rate': 40, 'additional_threshold': 33300},
    2007: {'personal_allowance': 0, 'basic_rate': 10, 'basic_threshold': 2230, 'higher_rate': 22, 'additional_rate': 40, 'additional_threshold': 34600},
    2008: {'personal_allowance': 6035, 'basic_rate': 20, 'basic_threshold': 34800, 'higher_rate': 40, 'additional_rate': None, 'additional_threshold': None},
    2009: {'personal_allowance': 6475, 'basic_rate': 20, 'basic_threshold': 37400, 'higher_rate': 40, 'additional_rate': None, 'additional_threshold': None},
    2010: {'personal_allowance': 6475, 'basic_rate': 20, 'basic_threshold': 37400, 'higher_rate': 40, 'additional_rate': 50, 'additional_threshold': 150000},
    2011: {'personal_allowance': 7475, 'basic_rate': 20, 'basic_threshold': 3500, 'higher_rate': 40, 'additional_rate': 50, 'additional_threshold': 150000},
    2012: {'personal_allowance': 8105, 'basic_rate': 20, 'basic_threshold': 34371, 'higher_rate': 40, 'additional_rate': 50, 'additional_threshold': 150000},
    2013: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 32010, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    2014: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 31865, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    
    2015: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 31785, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    2016: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 32000, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    2017: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 33500, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    2018: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 34500, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    2019: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 37500, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    2020: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 37500, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    2021: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 37700, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    2022: {'personal_allowance': 9440, 'basic_rate': 20, 'basic_threshold': 37700, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 150000},
    
    2023: {'personal_allowance': 12570, 'basic_rate': 20, 'basic_threshold': 37700, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 125140},
    2024: {'personal_allowance': 12570, 'basic_rate': 20, 'basic_threshold': 37700, 'higher_rate': 40, 'additional_rate': 45, 'additional_threshold': 125140},
}

def calculate_tax(year, salary):
    if year not in tax_data:
        raise ValueError(f"Tax data for the year {year} is not available.")
    
    data = tax_data[year]
    personal_allowance = data['personal_allowance']
    
    # Adjust personal allowance for high incomes
    if salary > 100000:
        personal_allowance = max(0, personal_allowance - (salary - 100000) / 2)
    
    taxable_income = max(0, salary - personal_allowance)
    tax = 0

    # Calculate tax for basic rate
    if taxable_income > 0:
        basic_taxable = min(data['basic_threshold']-personal_allowance, taxable_income)
        tax += basic_taxable * data['basic_rate'] / 100
        taxable_income -= basic_taxable
        
    # Calculate tax for higher rate
    if taxable_income > 0:
        higher_taxable =  min(data["additional_threshold"]-data["basic_threshold"], taxable_income)
        tax += higher_taxable * data['higher_rate'] / 100
        taxable_income -= higher_taxable

    # Calculate tax for additional rate
    if data['additional_rate'] and taxable_income > 0:
        tax += taxable_income * data['additional_rate'] / 100
    
    return round(tax, 2)

# Example usage
if __name__ == "__main__":
    year = 2013
    salary = 156000
    tax = calculate_tax(year, salary)
    print(tax)