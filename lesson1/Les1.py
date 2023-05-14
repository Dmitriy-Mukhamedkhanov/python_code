
def sales_sum(sales):
    total_sales = sum(sales)
    everage = total_sales/len(sales)
    max_sales = max(sales)
    return total_sales,everage,max_sales


sales = [1200, 1500, 1000, 1800, 900, 1300]
total, everage, max_sales = sales_sum(sales)

print(f'сумма продаж {total}\n '
      f'среднее значение {everage}\n'
      f'максимальные продажи {max_sales}')