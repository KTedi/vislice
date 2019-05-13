Stevilo_dovoljenih_napak = 10
Pravilna_crka = '+'
Ponovljena_crka = 'o'
Napacna_crka = '-'
Zmaga = 'W'
Poraz = 'X'

class Igra:
    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke
    def napacne_crke(self):
        sez = []
        for crka in self.crke:
            if crka not in self.geslo:
                seznam.append(crka)
            return seznam
        
    def pravilne_crke(self):
        sez = []
        for crka in self.crke:
            if crka in self.geslo:
                seznam.append
            return seznam

        
    def stevilo_napak(self):
        return len(napacne_crke)

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.geslo:
                return False
            return True
        
           
    def poraz(self):
        if stevilo_napak > stevilo_dovoljenih_napak:
            return poraz

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka = ''
        else:
            niz += '_'
            return niz


    def nepravilni_ugibi(self):
        niz = ''
        for crka not in self.geslo:
            if crka in self.crke:
                crka = ' '
        else:  
            return niz

    def ugibaj(self):
        if crka in self.geslo:
            return pravilne_crke(self)
        if crka in :
            return 
        if crka not in self.geslo:
            return napacne_crke(self)
        if crka in self.geslo:
            return zmaga(self)
        if crka not in self.geslo:
            return poraz(self)
         

   