# kurt

Dit zijn twee script voor het automatiseren van het reserveren op het KURT systeem.
reservation.py is het script voor het reserveren van een plek.
check_in.py is het script voor het inchecken van je plek.

Er moet nog een bestand aangemaakt worden genaamd "properties.py" voor het toevoegen van je username en password van Toledo en het id van je plek.
Deze template kan gebruikt worden:
```
username = "mijn_naam"
password = "mijn_wachtwoord"

id = "301113"
```

Nadat dit is voltooid, moet je bij deze twee scripts een tijds trigger opzetten zodat ze elke dag op het juiste uur worden uitgevoerd.
