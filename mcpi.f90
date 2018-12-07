! mcpi.f90
! routines for estimating pi using Monte Carlo
      subroutine pi_with_coords(n, x, y, pos, cpi)
      implicit none
      integer :: n,i
      double precision cpi
      double precision :: x(n), y(n)
      integer :: pos(n)
Cf2py intent(in) n
Cf2py intent(out) cpi
Cf2py intent(out) x
Cf2py intent(out) y
Cf2py intent(out) pos
C2fpy depends(n) x
C2fpy depends(n) y
Cf2py depends(n) pos
Cf2py depends(n) cpi

      call random_number(x)
      call random_number(y)

      do i=1,n
        if (sqrt(x(i) ** 2 + y(i) ** 2).le.1) then
           pos(i) = 1
        else
            pos(i) = 0
        endif
      enddo
      cpi = 4 * sum(pos) / real(n)
      end

      double precision function calc_pi(n)
! compute pi using n random draws
      implicit none
      integer :: n, i, s
      double precision :: x, y
Cf2py intent(in) n

      s = 0
      do i=1,n
      call random_number(x)
      call random_number(y)
      if (sqrt(x ** 2 + y ** 2).le.1) then
          s = s + 1
      endif
      enddo
      calc_pi = 4 * real(s) / real(n)
      end

      subroutine sample_pi(ns, samples, bins)
          implicit none
          integer :: ns, i
          integer :: samples(ns)
          double precision :: bins(ns), calc_pi
Cf2py intent(in) ns
Cf2py intent(in) samples
Cf2py intent(out) bins
Cf2py depends(samples) bins

          do i=1,ns
          bins(i) = calc_pi(samples(i))
          enddo
          end
