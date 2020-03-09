from distutils.core import setup
import py2exe

import py2exe
import matplotlib
import FileDialog
setup(windows=["base.py"],
options={
                "py2exe": {
                    # 'bundle_files': 1,
                    # 'compressed': True,
                    "includes": ['scipy', 'scipy.integrate', 'scipy.special.*', 'scipy.linalg.*',
                                 'scipy.interpolate.*','scipy.sparse.csgraph._validation','scipy._lib.messagestream',
                                 'pandas._libs.tslibs.conversion.*','pandas._libs.tslibs.np_datetime',
                                 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype',
                                 'pandas._libs.skiplist'],
                    "dll_excludes": ["api-ms-win-crt-heap-l1-1-0.dll",
                                 "api-ms-win-crt-string-l1-1-0.dll",
                                 "api-ms-win-crt-runtime-l1-1-0.dll",
                                 "api-ms-win-crt-stdio-l1-1-0.dll",
                                 "MSVCP90.dll",
                                 "api-ms-win-crt-locale-l1-1-0.dll",
                                 "api-ms-win-crt-filesystem-l1-1-0.dll",
                                 "api-ms-win-crt-utility-l1-1-0.dll",
                                 "api-ms-win-crt-environment-l1-1-0.dll",
                                 "api-ms-win-crt-time-l1-1-0.dll",
                                 "api-ms-win-core-delayload-l1-1-0.dll",
                                 "api-ms-win-core-processthreads-l1-1-0.dll",
                                 "api-ms-win-core-delayload-l1-1-1.dll",
                                 "api-ms-win-core-string-obsolete-l1-1-0.dll",
                                 "api-ms-win-core-profile-l1-1-0.dll",
                                 "api-ms-win-core-libraryloader-l1-2-0.dll",
                                 "api-ms-win-core-errorhandling-l1-1-0.dll",
                                 "api-ms-win-core-sysinfo-l1-1-0.dll",
                                 "api-ms-win-security-activedirectoryclient-l1-1-0.dll",
                                 "api-ms-win-core-heap-l2-1-0.dll",
                                 "api-ms-win-crt-conio-l1-1-0.dll",
                                 "libdet.3BHIBQXTJMMGQN3SDRUDY25WG7VDMC4N.gfortran-win32.dll",
                                 "libdop853.ZDB77F5S63EPO7WWG3LICXZSBW2LFM2N.gfortran-win32.dll",
                                 "libchkder.ACKDBOJBSJX62PBVWDOLR7SBBWNGB4T2.gfortran-win32.dll",
                                 "api-ms-win-crt-convert-l1-1-0.dll","api-ms-win-crt-math-l1-1-0.dll",
                                 "libdcosqb.TV5LOFJPDPVMTSGCBM3KOND62W3EURSE.gfortran-win32.dll",
                                 "libbispeu.OAANPWJKKXZRFOCA7BPAXPEXKORTJQMF.gfortran-win32.dll",
                                 "libwrap_dum.3DPPYO6VZDKKMFVLD3FRJRX6RHXAYX6J.gfortran-win32.dll",
                                 "libdfitpack.7IGKXGLR635JIUOZ2GVKCR4V7FH2643M.gfortran-win32.dll",
                                 "libdgamln.6AVEGLY3BWK2YI3L4IPCL7OOYUV6MOU7.gfortran-win32.dll",
                                 "libdcsrch.CTD6WPTKUW4MYYPI2KYOJ4427ZGGSXEQ.gfortran-win32.dll",
                                 "libgetbreak.WPO2FIAZLYYRXHEQSE55KAQRV2NOWW6B.gfortran-win32.dll",
                                 "libnnls.GX3LBH56JRQ7JMAOG7UBTDQJYFS6BPRN.gfortran-win32.dll",
                                 "libdcosqb.LDQTPBRX7W2KNZWNR4EQESJVKPKJ5HCX.gfortran-win32.dll",
                                 "libwrap_dum.67NPECI2CNH2S2WKFMJ5USH4AMJF5H5G.gfortran-win32.dll",
                                 "libansari.Q4BAGRNANLWD2YZJOKYPOAUIOLXW2LXK.gfortran-win32.dll",
                                 "libblkdta00.WPFFHKUMFZS5GV5FHYTO2Y3VX25OITRW.gfortran-win32.dll",
                                 "liblbfgsb.NYZHLRFFJMG2JIFXAZL2YJB762T7ZIRR.gfortran-win32.dll",
                                 "libcobyla2.MZIYBZPTVTYIHRT7JCIZN4FNMM5IPWLD.gfortran-win32.dll",
                                 "libdqag.GML2TKAFHWUOEYMC65VVAUUPGOKL3T47.gfortran-win32.dll",
                                 "libvode.DNH7SNO5ZKIXEPXHU5X6YCWGHFEVOLZO.gfortran-win32.dll",
                                 "lib_arpack-.BPMNVNEGY2NWLPV3WUAHJCDRO3UNCCLV.gfortran-win32.dll",
                                 "libmvndst.T3W46BXOB6EPBV4YHL2PNOCKNY2QSUQO.gfortran-win32.dll",
                                 "libslsqp_op.PY4IBHJ4EFVQXCMTZF6MCCENNULFVBJB.gfortran-win32.dll",
                                 "libspecfun.I7OMDT5L33XVQM2MTW5AACQJUBYEOUFN.gfortran-win32.dll",

                                 ]
                         },

        },data_files=matplotlib.get_py2exe_datafiles()),