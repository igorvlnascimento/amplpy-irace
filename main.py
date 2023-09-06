import argparse
import logging
import sys
from amplpy import AMPL

def main(MOD_FILE, DAT_FILE, INTTOL, GAP, GAPABS, DATFILE):
	# just a test
	# score = MUTPB*POP/100
	# score = float(score)
	# score = score - float(CXPB)
	# if score < 0:
	# 	score = 0

	ampl = AMPL()
	ampl.read(MOD_FILE)
	ampl.read_data(DAT_FILE)
	# tickers, cov_matrix = # ... pre-process data in Python
	# ampl.set["A"] = tickers
	# ampl.param["S"] = pd.DataFrame(
	# 	cov_matrix, index=tickers, columns=tickers
	# )
	ampl.option["solver"] = "gurobi"
	ampl.option["gurobi_options"] = f"mipgap={GAP}, mipgapabs={GAPABS}, inttol={INTTOL}"
	ampl.solve()

	score = ampl.get_objective('Total_Cost').value()

	# save the fo values in DATFILE
	with open(DATFILE, 'w') as f:
		f.write(str(score))

if __name__ == "__main__":
	# just check if args are ok
	with open('args.txt', 'w') as f:
		f.write(str(sys.argv))
	
	# loading example arguments
	ap = argparse.ArgumentParser(description='Feature Selection using GA with DecisionTreeClassifier')
	ap.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
	# Theses is the model and data files from AMPL language
	ap.add_argument('--mod', dest='mod', type=str, required=True, help='Model file')
	ap.add_argument('--dat', dest='dat', type=str, required=True, help='Data file')
	# 3 args to test values
	# It's possible to use any other options for GUROBI algorithm to optimize (https://dev.ampl.com/solvers/gurobi/options.html)
	ap.add_argument('--inttol', dest='inttol', type=float, required=True, help='Feasibility tolerance')
	ap.add_argument('--gap', dest='gap', type=float, required=True, help='Max. relative MIP optimality gap')
	ap.add_argument('--gapabs', dest='gapabs', type=float, required=True, help='Max. absolute MIP optimality gap')
	# 1 arg file name to save and load fo value
	ap.add_argument('--datfile', dest='datfile', type=str, required=True, help='File where it will be save the score (result)')

	args = ap.parse_args()
	logging.debug(args)
	# call main function passing args
	main(args.mod, args.dat, args.inttol, args.gap, args.gapabs, args.datfile)