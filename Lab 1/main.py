# 
# File:			main.py
# Author:		Jackson Petty <jackson.petty@yale.edu>
# Description:	All code necessary for Lab 1
# 

from astropy.cosmology import WMAP7, Planck15
from matplotlib import pyplot as plt
import numpy as np

def problem_one():
	"""
	Create a plot of Angular Diameter Distance vs Redshift
	for WMAP7 and Planck15 cosmologies
	"""
	redshift = np.linspace(0, 1, 1000)
	wmap_da = WMAP7.angular_diameter_distance(redshift)
	planck_da = Planck15.angular_diameter_distance(redshift)

	plt.rc('text', usetex=True) 
	plt.rc('font', family='serif')

	fig = plt.figure()
	ax_1 = fig.add_subplot(111)
	# ax_2 = ax_1.twiny()
	ax_1.plot(redshift, wmap_da, label="WMAP7")
	ax_1.set_ylabel("Angular Diameter Distance ($d_A$)")
	ax_1.set_xlabel("Redshift ($z$)")

	plt.title("Angular Diameter Distance vs Redshift for WMAP7 and Planck15")
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

	plt.show()

def problem_two():
	d1 = np.random.normal(0, 1, 200)
	d2 = np.random.normal(0, 2, 200)
	d3 = np.random.normal(1, 1, 200)

	plt.rc('text', usetex=True) 
	plt.rc('font', family='serif')

	fig = plt.figure()

	ax_one = fig.add_subplot(321)
	ax_two = fig.add_subplot(322)
	ax_one.plot(range(0,200), d1, label="$\sigma=1,\,\mu=0$")
	count, bins, ignored = plt.hist(d1, 30, normed=True)
	ax_two.plot(bins, 1/(1 * np.sqrt(2 * np.pi)) * np.exp( - (bins - 0)**2 / (2 * 1**2) ), linewidth=2, color='r')

	ax_three = fig.add_subplot(323)
	ax_four = fig.add_subplot(324)
	ax_three.plot(range(0,200), d2, label="$\sigma=2,\,\mu=0$")
	count, bins, ignored = plt.hist(d2, 30, normed=True)
	ax_four.plot(bins, 1/(2 * np.sqrt(2 * np.pi)) * np.exp( - (bins - 0)**2 / (2 * 2**2) ), linewidth=2, color='r')

	ax_five = fig.add_subplot(325)
	ax_six = fig.add_subplot(326)
	ax_five.plot(range(0,200), d3, label="$\sigma=1,\,\mu=1$")
	count, bins, ignored = plt.hist(d3, 30, normed=True)
	ax_six.plot(bins, 1/(1 * np.sqrt(2 * np.pi)) * np.exp( - (bins - 1)**2 / (2 * 1**2) ), linewidth=2, color='r')
	
	# plt.plot(range(0,200), d1, label="$\sigma=1,\,\mu=0$")
	# plt.plot(range(0,200), d2, label="$\sigma=2,\,\mu=0$")
	# plt.plot(range(0,200), d3, label="$\sigma=1,\,\mu=1$")

	# count, bins, ignored = plt.hist(d1, 30, normed=True)
	# plt.plot(bins, 1/(1 * np.sqrt(2 * np.pi)) * np.exp( - (bins - 0)**2 / (2 * 1**2) ), linewidth=2, color='r')

	plt.show()

def problem_three():
	mu = 1
	sigma = 0

	avg_avg = []
	avg_med = []
	avg_hlf = []

	for i in range(0,10**4):
		values = np.random.normal(sigma,mu,100)
		avg_avg.append(mu - np.average(values))
		avg_med.append(mu - np.median(values))
		avg_hlf.append(mu - 0.5*(min(values) + max(values)))
	
	tests = [avg_avg, avg_med, avg_hlf]

	for t in tests:
		print(np.average(t))
	
	plt.rc('text', usetex=True) 
	plt.rc('font', family='serif')

	# plt.plot(range(0,10**4), avg_avg, label="Test")
	count, bins, ignored = plt.hist(avg_avg, 100, normed=True)
	# ax_two.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - 0)**2 / (2 * 1**2) ), linewidth=2, color='r')
	plt.show()


def main():
	# redshift = np.linspace(0, 1, 1000)
	# wmap_da = WMAP7.angular_diameter_distance(redshift)
	# planck_da = Planck15.angular_diameter_distance(redshift)

	# # fig = plt.figure(figsize=(12,10))
	# # ax = fig.add_subplot(111)
	# # ax.plot(wmap_da, redshift)
	# # ax.set_xlabel("$d_a$")
	# # ax.plot(planck_da, redshift)

	# # plt.rc('text', usetex=True)
	# # plt.rc('font', family='serif')
	# plt.plot(planck_da, redshift)
	# plt.plot(wmap_da, redshift)
	# plt.xlabel("Angular Diameter ($d_A$)")
	# plt.ylabel("Redshift ($z$)")
	# plt.show()

	# # fig.savefig('test.png')
	# problem_one()
	problem_three()

if __name__ == '__main__':
	main()