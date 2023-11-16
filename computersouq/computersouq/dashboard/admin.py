from django.contrib import admin
from .models import invoice, Creditor_debtor_accounts, transaction
@admin.register(invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display= ['id', 'Name', 'Phone_Number']
    list_display_links= ['id', 'Name']
    search_fields= ['Name', 'Phone_Number', 'id']
    list_filter= ['DateTime', 'id'] 
    
@admin.register(Creditor_debtor_accounts)
class Creditor_debtor_accountAdmin(admin.ModelAdmin):
    list_display= ['id', 'Name', 'Phone_Number']
    list_display_links= ['id', 'Name']
    search_fields= ['Name', 'Phone_Number', 'id']
    list_filter= ['id'] 
admin.site.register(transaction)