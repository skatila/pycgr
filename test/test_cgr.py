from pycgr.dnacgr import fasta_reader, mk_cgr
TEST_F = "test.fasta"

FASTAS = [ i for i in fasta_reader(TEST_F)]
# CGR for both lower and upper should be same
TEST_SEQ_LOWER = "atgatgaaatagagagactttat"
TEST_SEQ_UPPER = "ATGATGAAATAGAGAGACTTTAT"
CGR = [(0.25, 0.25),
 (0.625, 0.125),
 (0.8125, 0.5625),
 (0.40625, 0.28125),
 (0.703125, 0.140625),
 (0.8515625, 0.5703125),
 (0.42578125, 0.28515625),
 (0.212890625, 0.142578125),
 (0.1064453125, 0.0712890625),
 (0.55322265625, 0.03564453125),
 (0.276611328125, 0.017822265625),
 (0.6383056640625, 0.5089111328125),
 (0.31915283203125, 0.25445556640625),
 (0.659576416015625, 0.627227783203125),
 (0.3297882080078125, 0.3136138916015625),
 (0.6648941040039062, 0.6568069458007812),
 (0.3324470520019531, 0.3284034729003906),
 (0.16622352600097656, 0.6642017364501953),
 (0.5831117630004883, 0.33210086822509766),
 (0.7915558815002441, 0.16605043411254883),
 (0.8957779407501221, 0.08302521705627441),
 (0.44788897037506104, 0.04151260852813721),
 (0.7239444851875305, 0.020756304264068604)]
def test_fasta_reader_1():
	assert(FASTAS[0][0] == "fasta1")

def test_fasta_reader_2():
	assert(FASTAS[0][1] == TEST_SEQ_LOWER)

def test_cgr_lower():
	assert([i[1] for i in mk_cgr(TEST_SEQ_LOWER)] == CGR)

def test_cgr_upper():
	assert([i[1] for i in mk_cgr(TEST_SEQ_UPPER)] == CGR)
