      REAL FUNCTION FUNC(X)
      COMMON/PAWPAR/PAR(5)
      if(x.lt.par(1)) then
        FUNC=0.0
        return
      endif
      if(x.gt.par(3)) then
        FUNC=0.0
        return
      endif
      if((x.gt.par(1)).and.(x.lt.par(2))) then
        FUNC=par(4)
        return
      endif
      if((x.gt.par(2)).and.(x.lt.par(3))) then
        FUNC=par(5)
        return
      endif
      END


