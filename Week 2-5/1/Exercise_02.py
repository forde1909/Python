income = 37000
single_person_tax_allowance = 36800
taxable_at_20_persent = income - single_person_tax_allowance
taxable_at_40_persent = income - taxable_at_20_persent
persent_tax_20 = taxable_at_20_persent * .2
persent_tax_40 = taxable_at_40_persent * .4
total_tax = persent_tax_20 + persent_tax_40
print(total_tax)
