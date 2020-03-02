def fEa(self):  
  Tarvh, Fav, Tav, Tarvs
  Fav = fFa()
  Tarvh = Fav
  Tarvs = fTar(Tarvh)
  Tav = Tarvs
  return Tav
   
def fEar(self, Earvh):
  Ear1vh, Tav, Earvs, Ear1vs
  if ( tk.cat == mais ):
     tk = nextTk()
     Tav = fTa()
     Ear1vh = Earvh + Tav
     Ear1vs = fEar(Ear1vh)
     Earvs = Ear1vs
     return Earvs
  if ( tk.cat == menos ):
      tk = nextTk()
      Tav = fTa()
      Ear1vh = Earvh - Tav
      Ear1vs = fEar(Ear1vh)
      Earvs = Ear1vs
      return Earvs
            
  Ear1vs = Ear1vh
  Earvs = Ear1vs
  return earvs

def fTa(self):
  Tarvh, Fav, Tav, Tarvs
  Fav = fFa()
  Tarvh = Fav
  Tarvs = fTar(Tarvh)
  Tav = Tarvs
  return Tav
   
def fTar (self, Tarvh):
  Tar1vh, Fav, Tarvs, Tar1vs
  if ( tk.cat == vezes )
    tk = nextTk()
    Fav = fFa()
    Tar1vh = Tarvh * Fav
    Tar1vs = fTar(Tar1vh)
    Tarvs = Tar1vs
    return Tarvs
             
  if ( tk.cat == divisao ):
    tk = nextTk()
    Fav = fFa()
    Tar1vh = TArvh/Fav
    Tar1vs = fTar(Tar1vh)
    Tarvs = Tar1vs
    return Tarvs
        
  Tar1vs = Tar1vh
  Tarvs = Tar1vs
  return Tarvs
