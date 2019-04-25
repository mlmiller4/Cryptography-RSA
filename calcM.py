#!/usr/bin/python
import sys, hashlib, binascii

#def usage():
#    print """usage: python get_name_hash.py student_id
#    for example:
#    python get_name_hash.py qchenxiong3"""
#    sys.exit(1)

#if len(sys.argv) != 2:
#    usage()

#print hashlib.sha224(sys.argv[1]).hexdigest()

c = 0x1f66f24f4d7b6977fce338f7b9184f4a00ab80089b62f23f06c70712b58d12400a1eccd1152fce9cd0d00d791de1beef2f61c2c680f4492d4d5ef1a99b8638640e664f5ba2995da41be9e8534c606143648d89fbae85f08193192b24763c386a17c93b1e3f0923b6e5664bb1e4314c0b6ded761f34c941885bb65054aaddfac1
d = 0x697408d41b7526bd9953c4bcff147406594de899466be8f529361b972b32b020119028fb2a0537ab8735b7f47fc795e6cc89e5a0c080d578f7d7066d6112cb37976136ed085d7303d31f58b41ce36e62cb4d9282757fb5a68258de47a3c37d12af3ef7384029ece5a421866398157e0de227214d5fdd9fe1e041be9831f5981
N = 0xbcde6f52870f931ac0e0883b93c45bf9d3249de1a880632f075ad0850758491d3a3577bd6b205c93bfc1c1d5a1461cc1ab0b6ec7bd129f942f92bcc1b41b9f5da7e0689fbe651bf3452875ac30dbd7926494ba08550330ef72dcb11cae57bb8d926bc78ebcabbbf76b802393c0dc36f7e0f0f468cafd17168a0e538773f89945
e = "0x10001"

c_int = 48002763997475370079319422578682625238739671740484207446216673467948852627821413992849299496909458269849585250286809457117246495794482927969158076055459005431367071936807654665665164981966782848915230361224753655836383021487103274482449394457470133653277240255316180731202936796924340320568673453957355384860
d_int = 7900732432161163329694107205471696867207623872262028656281242194534131361009896914458287651642246822214750147254937182907395440199149559646999455497009615307216827676976524088308167401243313582725797162284728956277794933355640791471916001890634390210514761769203793404910658293021423687307488101760312807545
N_int = 93111005467819845556224187003236575721306607753360289884320044902568488942007842848921560479352262180810660025291641459486059155607204583813235625770098771033540717238258347061171502271311714639323345341391571615947935667981670480756554151795374736152414686413064288681717082733610314162486514500052478478111

#cd = pow(c_int, d_int)
print "Calculating msg..."
#tmp = pow(c_int, d_int)
msg = pow(c, d, N)
print "msg calculated: "
print hex(msg)

##c_conv = 9.0863639822818*(10^37)
##d_conv = 2.3928265667039*(10^37)
##N_conv = 1.7624828571983*(10^38)
##e_conv = 65537
##
##cd = pow(c_conv, d_conv)
##
##m = cd % N_conv
##
##print "m = "
##print m
##
##hex = "0568ab7874f75fdc023240431a2ffad24"
##msg = binascii.unhexlify(hex)
##print msg

##c_int = int(c, 16)
##d_int = int(d, 16)
##N_int = int(N, 16)
##e_int = int(e, 16)

##print "c_int = "
##print c_int
##print ""
##print "d_int = "
##print d_int
##print ""
##print "N_int = "
##print N_int
##
##cd = c_int^d_int
##
##print ""
##print "cd = "
##print cd
##
##m = cd % N_int
##
##print ""
##print "m = "
##print m
##
##hex_m = hex(m)
##msg = binascii.unhexlify(hex_m[2:-1])
##
##print ""
##print "msg = "
##print msg

##print ""
##print "plain ="
##
##plain = [chr((char ** d) % N_int) for char in c]
##print ''.join(plain)

##print "c = "
##print hashlib.sha224(c).hexdigest()
##print ""
##print "d = "
##print hashlib.sha224(d).hexdigest()
##print ""
##print "N = "
##print hashlib.sha224(N).hexdigest()

##print ""
##print "c converted: "
##print int(c, 16)

#cd = hashlib.sha224(c).hexdigest()^hashlib.sha224(d).hexdigest()

#print "cd ="
#print cd




#msg = tmp % N

#print msg

