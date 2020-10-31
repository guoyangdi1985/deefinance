from django.db import models


class CreditCard(models.Model):
    card_number = models.CharField(max_length=20)
    expiration = models.CharField(max_length=7)
    security_code = models.IntegerField()
    billing_address = models.CharField(max_length=50)
    card_holder_name = models.CharField(max_length=30)


class BankDraft(models.Model):
    bank_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)
    routing_number = models.CharField(max_length=20)
    account_hold_name = models.CharField(max_length=30)

    def __str__(self):
        return self.bank_name


class Credential(models.Model):
    creditcards = models.ManyToManyField(CreditCard, blank=True, null=True)
    bankdrafts = models.ManyToManyField(BankDraft, blank=True, null=True)
    # payment_of_credential is the name of the service provider
    # to which I submit credential.
    payment_of_credential = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.payment_of_credential
