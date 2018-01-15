"""
$ ./script.py input_file previously_generated file

need previously generated file to get default values from in case you don't want to change anything
"""

DEFAULT_INPUTS = {
    "file_name": "KrDD_2D_0.8_0.02_1eV",
    "twfn": "200.0e-9",
    "dt": "1.0e-13",
    "dtmax": "1.0e-9",
    "dtstopr": "1.0e-20",
    "cyl": "1.",
    "eoson": "true",
    "trackon": "true",
    "tsplit": "1",
    "hydron": "true",
    "rotate": "true",
    "strength": "false",
    "jouhtmlt": "1.0",
    "hallon": "false",
    "neutrons": "true",
    "alphaheat": "true",
    "aresvac": "1.0e4",
    "theb": "0.5",
    "courmax": "0.99",
    "rmvolrm": "0.3",
    "volratm": "0.7",
    "donor": "false",
    "meshon": "false",
    "zeroghcl": "false",
    "niter": "3",
    "eqvol": "0.01",
    "orthog": "1.0e10",
    "nsmooth": "5",
    "eps": "1.0e-6",
    "conserv": "0.0",
    "magon": "true",
    "brbzon": "true",
    "radiate": "true",
    "radmodl": "neqdiff",
    "radcupl": "integrtd",
    "radflxlt": "true",
    "radsize": "0.001",
    "ciron": "true",
    "flxcirc": "true",
    "multgrd": "false",
    "thmldif": "true",
    "anisot": "true",
    "mgmodet": "converge",
    "nthrmax": "6000",
    "tdrelax": "1",
    "curthrmx": "1.0e4",
    "tdtol": "1.0e-4",
    "bdiff": "true",
    "mgmode": "converge",
    "itmaxrd": "6000",
    "rdrelax": "1.0",
    "rdtol": "1.0e-4",

    "volttype(1)": "zebra",
    "circtype(1)": "rlc",
    "exres(1)": "2.3",
    "exind(1)": "69.0e-9",
    "capac(1)": "0.0",
    "current(1)": "0.0",

    "dtpost":,
    "hdfon":,
    "ncycpost:":,

    "intty(1)":,
    "intty(2)":,
    "ncyctty":,
    
    "dthist":,
    "histenrg":,


    }

def populate_file(input_vars=DEFAULT_INPUTS):
    input_file = """
    Staged pinch of Kr liner profile obtained from experimental measurement.
    %(file_name)s
     
    ! 01 - 1D w/ sesame tables
    ! 02 - max diff set to limit tdiff using 20 microns
    ! 03 - etamax 6.0e3 throughout
     
    ! Simple Z-Pinch test case using PBFZ refurbished class machine.
    ! ideal MHD
     $contrl
     
    ! time control parameters
        twfn       = %(twfn)s,    ! problem end time
        dt         = %(dt)s,     ! initial time step
        dtmax      = %(dtmax)s,      ! maximum time step
        dtstopr    = %(dtstopr)s,     ! minimum time step, stop if dt < (dtstopr * t)
     
    ! general problem configuration
        cyl        = %(cyl)s,          ! cylindrical geometry
        eoson      = .%(eoson)s.,      ! calculate EOS
        trackon    = .%(trackon)s.,      ! allow materials to mix
        tsplit     = %(tsplit)s,           ! ion and electron temperatures calculated separat
        hydron     = .%(hydron)s.,      ! solve ideal MHD
        rotate     = .%(rotate)s.,      ! allows the out-of-plane component of velocity t
        strength   = .%(strength)s.,     ! switch for strength-of-materials package
        jouhtmlt   = %(jouhtmlt)s,         ! multiplier for Ohmic heating
        hallon     = .%(hallon)s.,     ! switch to include Hall effect in resistive diffu
        neutrons   = .%(neutrons)s.,      ! calculate neutron yield
        alphaheat  = .%(alphaheat)s.,      ! calculate alpha-particle heating
        aresvac    = %(aresvac)s,       ! Anomalous diffusivity in vacuum region
     
    ! mesh solver parameters
        theb       = %(theb)s,         ! use centered time difference
        courmax    = %(courmax)s,        ! max(dtcour) = courmax * (t_Alfven + t_acoustic)
        rmvolrm    = %(rmvolrm)s,         ! dtc set such that no more than rmvolrm of a cell
                                  ! convected in one cycle
        volratm    = %(volratm)s,         ! dtvol set such that no cell's volume changes by
                                  ! (1 - volratm) in one cycle
        donor      = .%(donor)s.,     ! use default Van-Leer second-order scheme
     
    ! ideal mesh parameters
        meshon     = .%(meshon)s.,      ! compute ideal mesh each computational cycle
        zeroghcl   = .%(zeroghcl)s.,     ! if true, makes ghost cells on non-shared boundar
    !   nigen      = 10,          ! # of initial Jacobi iterations of ideal mesh gen
        niter      = %(niter)s,           ! # of Jacobi iterations of ideal mesh generator i
        eqvol      = %(eqvol)s,        ! overall multiplier of adaptivity weight function
        orthog     = %(orthog)s,      ! larger values attempt to make cells orthogonal
        nsmooth    = %(nsmooth)s,           ! number of smoothing steps applied to the adaptiv
    !   wrelax     = 1,           ! smooths adaptivity function of wrelax # of cells
     
    ! HYDRO solver parameters
    !    mu         = 1.0,         ! coefficient for artificial viscosity, spreads s
                                  ! mu # of cells
        eps        = %(eps)s,      ! convergence tolerance for relative error in HYDR
        conserv    = %(conserv)s,         ! if non-zero, force the code to approximately con
                                  ! and magnetic energy
     
    ! Magnetic field solver
        magon      = .%(magon)s.,      ! calculate magnetic fields
        brbzon     = .%(brbzon)s.,      ! include the in-plane components of the magnetic
     
    ! Radiation model parameters
        radiate    = .%(radiate)s.,      ! compute radiative losses
        radmodl    = '%(radmodl)s',  ! calculate losses due to emission, i.e. optically
        radcupl    = '%(radcupl)s',
    !    radcupl    = .true.,
        radflxlt   = .%(radflxlt)s.,
        radsize    = %(radsize)s,
    !    flxlmt = 0.0,
     
    ! Circuit driver paraeters
        ciron      = .%(ciron)s.,      ! compute in-plane driving electric current across
        flxcirc    = .%(flxcirc)s.,      ! use magnetic flux to calculate load voltage in p
     
    ! Multigrid parameters
        multgrd    = .%(multgrd)s.,     ! switch to enable multigrid
     
    ! Thermal diffusion solver parameters
        thmldif    = .%(thmldif)s.,      ! compute thermal diffusion
        anisot     = .%(anisot)s.,      ! include B-field-induced anisotropic effects
        mgmodet    = '%(mgmodet)s',  ! method for progressing through multigrid levels
        nthrmax    = %(nthrmax)s,        ! max # of iterations of solver per cycle
        tdrelax    = %(tdrelax)s,           ! coefficient of relaxation factor applied to temp
        curthrmx   =%(curthrmx)s,
                                  ! multigrid level
        tdtol      = %(tdtol)s,      ! convergence toleranc for relative error in tempe
                                  ! multigrid level
    !   tdtolcg    = 0.25,        ! convergence criterion for the maximum ratio of r
                                  ! temperature on a coarse grid to that on the adja
    !    arttherm   = .false.,      ! smoother for an artificla thermal conductivity
                                  ! anomalous heating across shocks
    !    artthmlt   = 3.0,         ! overall multiplier of the artificial thermal co
     
    ! Magnetic diffusion solver parameters
        bdiff      = .%(bdiff)s.,      ! computer resistive diffusion of B-field
        mgmode     = '%(mgmode)s',  ! method for progressing through multigrid levels
        itmaxrd    = %(itmaxrd)s,        ! max # of iterations of solver per cycle
        rdrelax    = %(rdrelax)s,         ! relaxation multiplier applied to magnetic field
                                  ! multigrid level
        rdtol      = %(rdtol)s,      ! convergence tolerance for relative error in B-fi
                                  ! at the finest multigrid level
    !   rdtolcg    = 0.25,        ! convergence criterion for the maximum ratio of r
                                  ! magnetic induction on a coarse grid to that on a
     $end
     
    ! ***************************
     
     $curnt
        volttype(1) = 'zebra',    ! Zebra-style external circuit, voltage profile fo
        circtype(1) = 'rlc',      ! Single-loop RL circuit
        exres(1)    = 2.3,        ! R0
        exind(1)    = 69.0e-9,    ! L0
        capac(1)    = 0.0,        ! C0
        current(1)  = 0.0,        ! No initial current
     $end
     
    ! ***************************
     
     $output
    ! output file settings
        dtpost      = 1.0e-9,     ! Output every 5 ns during Ohmic heating phase
        hdfon       = .true.,     !
        ncycpost    = 100,
    ! terminal edit settings
        intty(1)    = 'edits,10', ! Write to edit file every 100 ns during Ohmic hea
        intty(2)    = '0       ',
        ncyctty     = 100,
    ! history file settings
        dthist      = 0.1e-9,
        histenrg    = .true.,     ! output energy budget equations to history file
     $end
     
    ! ***************************
     
     $ezphys
        gdvlg       = 0.00,       ! Eulerian simulation
        arsmodlg    = 'vacuum',   ! Anomalous resistivity set to aresvac
                                  ! if density < rofanom AND rofvac
        etamaxg     = 1.0e3,      ! tdiff of 66.67 fs over 20 micron,
                                  ! 20 micron/66.67 fs = 3.0x10^8 m/s
     $end
     
    ! ***************************
     
     $matmdl
        matnam(1)    = 'd',
        sesanam(1)   = 'd',
        eosmodl(1)   = 'tabular',
        nfemodl(1)   = 'constant',
          nfe0(1)    = 1.0,
        resmodl(1)   = 'tabular',
        tcnmodl(1)   = 'tabular',
        opacity(1)   = 'tabular',
     
        rofrad(1)    = 1.0e-7,
        rocrad(1)    = 1.0e3,
        rof(1)       = 3.32e-7,
        rofhyd(1)    = 3.32e-7,
        rofvac(1)    = 3.32e-7,
        rofanom(1)   = 3.32e-7,
        rofjoule(1)  = 3.32e-7,
        rofsiecp(1)  = 3.32e-7,
    !    sieiflr(1) = 1.0e6
    !    sieflr(1) = 1.0e6
        teflr(1)     = 1.0,
        tiflr(1)     = 1.0,
        tecap(1)     = 100.0e3,
        ticap(1)     = 100.0e3,
     
        gm1(1)       = 0.66666667,
        an(1)        = 1.0,
        aw(1)        = 2.0,
     
    !    matnam(2)    = 'ne',
    !    sesanam(2)   = 'ne-pl',
    !    eosmodl(2)   = 'tabular',
    !    mattabs(1,20)= 9541, 19541, 25414
    !    nfemodl(2)   = 'zfree2',
    !    opacity(2)   = 'neon',
    !    gm1(2)       = 0.66666667,
    !    an(2)        = 10.0,
    !    aw(2)        = 20.18,
     
    !    matnam(2)    = 'ar',
    !    sesanam(2)   = 'ar-mrc',
    !    eosmodl(2)   = 'tabular',
    !    mattabs(1,26)= 9517, 18517, 29171
    !    nfemodl(2)   = 'zfree3',
    !    opacity(2)   = 'tabular',
    !    gm1(2)       = 0.66666667,
    !    an(2)        = 18.0,
    !    aw(2)        = 39.948,
     
        matnam(2)     = 'kr',
        sesanam(2)    = 'kr',
        eosmodl(2)    = 'tabular',
        mattabs(1,31) = 5181, 18181, 28181,
        nfemodl(2)    = 'zfree3',
        opacity(2)    = 'tabular',
        gm1(2)        = 0.66666667,
        an(2)         = 36.0,
        aw(2)         = 83.8,
     
    !    matnam(2)    = 'xe',
    !    sesanam(2)   = 'xe',
    !    eosmodl(2)   = 'tabular',
    !    mattabs(3,30)= 5190, 15190, 25194,
    !    nfemodl(2)   = 'zfree3',
    !    opacity(2)   = 'xenon',
    !    gm1(2)       = 0.66666667,
    !    an(2)        = 54.0,
    !    aw(2)        = 131.3,
     
        resmodl(2)   = 'tabular',
        tcnmodl(2)   = 'tabular',
     
    !    atamin(2)    = 0,
    !    atamax(2)    = 0,
     
        rof(2)       = 1.0e-8,
        rofhyd(2)    = 1.0e-8,
        rofvac(2)    = 1.0e-7,
        rofanom(2)   = 1.0e-7,
        rofjoule(2)  = 1.0e-7,
        rofrad(2)    = 1.0e-8,
        rocrad(2)    = 1.0e3,
    !    rofsiecp(2)  = 1.0e-7,
        sieiflr(2) = 1.0e8
        sieflr(2) = 1.0e8
     
        teflr(2)     = 1.000,
        tiflr(2)     = 1.000,
        tecap(2)     = 100.0,
        ticap(2)     = 100.0,
     
     $end
     
    ! ***************************
     
     $ezgeom
     
        nblk = 5,
        npnts = 12,
     
        pointx(1)  = 0.000e-2, pointy(1)  = 1.000e-2,
        pointx(2)  = 0.100e-2, pointy(2)  = 1.000e-2,
        pointx(3)  = 0.100e-2, pointy(3)  = 0.000e-2,
        pointx(4)  = 0.000e-2, pointy(4)  = 0.000e-2,
     
        pointx(5)  = 0.900e-2, pointy(5)  = 1.000e-2,
        pointx(6)  = 0.900e-2, pointy(6)  = 0.000e-2,
     
        pointx(7)  = 1.200e-2, pointy(7)  = 1.000e-2,
        pointx(8)  = 1.200e-2, pointy(8)  = 0.000e-2,
     
        pointx(9)  = 1.700e-2, pointy(9)  = 1.000e-2,
        pointx(10) = 1.700e-2, pointy(10) = 0.000e-2,
     
        pointx(11) = 2.000e-2, pointy(11) = 1.000e-2,
        pointx(12) = 2.000e-2, pointy(12) = 0.000e-2,
     
        corners(1,1)  =  1,  2,  3,  4,
        corners(1,2)  =  2,  5,  6,  3,
        corners(1,3)  =  5,  7,  8,  6,
        corners(1,4)  =  7,  9, 10,  8,
        corners(1,5)  =  9, 11, 12, 10,
     
     $end
     
    ! **************************
     
     $inmesh
        icells(1)  = 100,     jcells(1)  = 64, ! 10 um
        icells(2)  = 100,     jcells(2)  = 64, ! 50 um
        icells(3)  = 50,      jcells(3)  = 64, ! 50 um
        icells(4)  = 50,      jcells(4)  = 64, ! 50 um
        icells(5)  = 10,      jcells(5)  = 64, ! 50 um
     
    !   gdvl(1) = 3.50,
    !   gdvl(2) = 3.50,
    !   gdvl(3) = 3.50,
    !   gdvl(4) = 3.50,
    !   gdvl(5) = 3.50,
     
    !   prsgrwt(1) = 1.0e9,
     
    !   prsgrwt(2) = 1.0e9,
     
    !   prsgrwt(3) = 1.0e8,
     
    !   prsgrwt(4) = 1.0e8,
     
    !   prsgrwt(5) = 1.0e7,
     
    !  The flags 'gaussian' and 'gausaxis' for roinit will apply a gaussian
    !  density variation in the radial direction. The density will remain
    !  uniform in the axial and azimuthal directions. The flag 'gaussian'
    !  places the center of the gaussian density profile in the center of
    !  the block. However, 'gausaxis' places the center on the left or right
    !  boundary depending on the sign of rnomden. If rnomden > 0.0, the
    !  gaussian profile is centered on left boundary, if rnomden < 0.0,
    !  the gaussian is centered on the right boundary.
     
    !  rnomden is used as the multiplying factor in the exponent of the
    !  gaussian function: ro = roi * exp(-abs(rnomden) * (r - r0)^2),
    !  where ro is the density at location r in the block and r0 is determined
    !  as above. NOTE: r and r0 are in meters.
     
        matnami(1)  = 'd',
        roinit(1) = 'cfdintp',
        roinitfile(1) = 'D2_density_180us.txt',
    !    roi(1)  = 3.0e-3,
    !    roinit(1) = 'gausaxis',
    !    rnomden(1) = 9.0e1,
    !    matnami(2)  = 'd',    roi(2)  = 4.0e-4,
    !    matnami(1)  = 'ar',
    !    roinit(1) = 'cfdintp',
        ldnblk(1) = 0.02,
        ropert(1)  = 'random',
        roprtam(1) = 0.01,
     
        matnami(2)  = 'd',
        roinit(2) = 'cfdintp',
        roinitfile(2) = 'D2_density_180us.txt',
        ldnblk(2) = 0.02,
        ropert(2)  = 'random',
        roprtam(2) = 0.01,
     
        matnami(3)  = 'kr',
        roinit(3) = 'cfdintp',
        roinitfile(3) = 'Ar_8ps_250.txt',
        ldnblk(3) = 0.8,
        ropert(3)  = 'random',
        roprtam(3) = 0.01,
     
        matnami(4)  = 'kr',
        roinit(4) = 'cfdintp',
        roinitfile(4) = 'Ar_8ps_250.txt',
        ldnblk(4) = 0.8,
        ropert(4)  = 'random',
        roprtam(4) = 0.01,
     
        matnami(5)  = 'kr',
        roinit(5) = 'cfdintp',
        roinitfile(5) = 'Ar_8ps_250.txt',
        ldnblk(5) = 0.8,
        ropert(5)  = 'random',
        roprtam(5) = 0.01,
     
        tempi(1)  =  1.0,    tioni(1)  = 1.0,
        tempi(2)  =  1.0,    tioni(2)  = 1.0,
        tempi(3)  =  1.0,    tioni(3)  = 1.0,
        tempi(4)  =  1.0,    tioni(4)  = 1.0,
        tempi(5)  =  1.0,    tioni(5)  = 1.0,
     
    ! Eulerian simulation, grid bcs unnecessary
     
    !   default grid bcs
     
    !   default grid ccs
     
    !   default hydrodynamic bcs (wall)
     
        hydbc(4,1) = 'axis',
        hydbc(2,5) = 'flowthru',
          roflow(2,5) = 1.0e-7,
          tflow(2,5)  = 1.0,
    !   radiation boundary condition
        radbc(2,5) = 'conduct',
          tradbdy(2,5) = 1.0,
     
    !   continuous magnetic BCs
        magbc(1,1) = 'contnutv', magbc(3,1) = 'contnutv', magbc(4,1) = 'axis',
        magbc(1,2) = 'contnutv', magbc(3,2) = 'contnutv',
        magbc(1,3) = 'contnutv', magbc(3,3) = 'contnutv',
        magbc(1,4) = 'contnutv', magbc(3,4) = 'contnutv',
        magbc(1,5) = 'contnutv', magbc(2,5) = 'insulatr', magbc(3,5) = 'contnutv',
        magxybc(2,5) = 'specfied',
          bybdy(2,5) = 0.0,
     
    !   default resistive BCs (symmetric)
     
    !   apply current on right side
        currcir(2,5) = 1,
     
    !   no initial magnetic field
        binit(1)  = 'none',  bxi(1)  = 0.0,  byi(1)  = 0.0,  bzi(1)  = 0.0,
        binit(2)  = 'none',  bxi(2)  = 0.0,  byi(2)  = 0.0,  bzi(2)  = 0.0,
        binit(3)  = 'none',  bxi(3)  = 0.0,  byi(3)  = 0.0,  bzi(3)  = 0.0,
        binit(4)  = 'none',  bxi(4)  = 0.0,  byi(4)  = 0.0,  bzi(4)  = 0.0,
        binit(5)  = 'none',  bxi(5)  = 0.0,  byi(5)  = 0.0,  bzi(5)  = 0.0,
     
    !   default thermbc, no conduction on outside walls
        thrmbc(4,1) = 'axis',
    !    ionvel(1) = .true.,
    !    ionvel(2) = .true.,
    !    ionvel(3) = .true.,
    !    ionvel(4) = .true.,
    !    ionvel(5) = .true.,
     
     $end
    ! **************************
     
     $modtim
        tmod = 110.0e-9,
     $end
     
     $output
    ! hdf output
        dtpost = 0.05e-9,
        ncycpost    = 100,
    ! terminal edits
        intty(1) = 'edits,10',
        intty(2) = '00      ',
        ncyctty = 100,
    ! history file
        dthist  = 0.05e-9,
     $end
     
     $modtim
        tmod = 165.0e-9,
     $end
     
     $output
        dtpost = 1.0e-9,
        dthist = 0.1e-9,
     $end

    """ % input_vars

    print input_file


populate_file()


































