from django.db import models


class Beroep(models.Model):
    id = models.IntegerField("BeroepID", primary_key=True)
    beroep = models.CharField("Beroep", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Beroep"
        verbose_name_plural = "Beroepen"

    def __str__(self):
        return self.beroep


class Basisgegevens(models.Model):
    id = models.IntegerField("ID", primary_key=True)
    nummer = models.CharField("Nummer", max_length=50, blank=True, null=True)
    persoon = models.CharField("Persoon", max_length=255, blank=True, null=True)
    alt_naam = models.CharField("Alternatieve naam", max_length=255, blank=True, null=True)
    bijnaam = models.CharField("Bijnaam", max_length=255, blank=True, null=True)
    beroep = models.ForeignKey(Beroep, on_delete=models.DO_NOTHING, blank=True, null=True)
    beroep_specifiek = models.CharField("Beroepspecifiek", max_length=255, blank=True, null=True)
    titel = models.CharField("Titel", max_length=255, blank=True, null=True)
    geboortedatum = models.CharField("Geboortedatum", max_length=255, blank=True, null=True)
    sterfdatum = models.CharField("Sterfdatum", max_length=255, blank=True, null=True)
    geografische_aanduiding = models.CharField("Geografische aanduiding", max_length=255, blank=True, null=True)
    beschrijving = models.CharField("Beschrijving", max_length=255, blank=True, null=True)
    portrait_histoire = models.BooleanField("Portrait Histoire", blank=True, null=True)
    kunstenaar = models.CharField("Kunstenaar", max_length=255, blank=True, null=True)
    begindatum = models.CharField("Begindatum", max_length=255, blank=True, null=True)
    einddatum = models.CharField("Einddatum", max_length=255, blank=True, null=True)
    afmetingen = models.CharField("Afmetingen", max_length=255, blank=True, null=True)
    techniek = models.CharField("Techniek", max_length=255, blank=True, null=True)
    reproductie = models.BooleanField("Reproductie", blank=True, null=True)
    originele_foto = models.BooleanField("Originele foto", blank=True, null=True)
    verblijfplaats = models.CharField("Verblijfplaats", max_length=255, blank=True, null=True)
    verblijfplaats_k = models.CharField("Verblijfplaats K", max_length=255, blank=True, null=True)
    zwart_wit = models.BooleanField("Zwart/wit", blank=True, null=True)
    kleur = models.BooleanField("Kleur", blank=True, null=True)
    kwaliteit_goed = models.BooleanField("Kwaliteit goed", blank=True, null=True)
    kwaliteit_slecht = models.BooleanField("Kwaliteit slecht", blank=True, null=True)
    verblijfplaats_r = models.CharField("Verblijfplaats R", max_length=255, blank=True, null=True)
    copyright = models.IntegerField("Copyright", blank=True, null=True)
    opmerking_copyright = models.CharField("Opmerkingen copyright", max_length=255, blank=True, null=True)
    opmerkingen = models.TextField("Opmerkingen", blank=True, null=True)
    filepath = models.CharField("Filepath", max_length=255, blank=True, null=True)
    jpg = models.CharField("Jpg", max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Basisgegevens"
        verbose_name_plural = "Basisgegevens"

    def __str__(self):
        return f"{self.persoon} ({self.titel})" or ""
