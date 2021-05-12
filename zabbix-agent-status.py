from pyzabbix import ZabbixAPI

def get_offline_zabbix_host():
	zapiurl = ZabbixAPI("http://zabbix-server-ip")   ### mention your zabbix server ip address here ###
	zapiurl.login("admin","zabbix") ### enter zabbix server login credentials ###

	host=zapiurl.host.get()
	count=0
	total=0

	for h in host:
		total=total+1
		if(int(h['available'])==2 and int(h['status'])==0):
			print(h['host']+"    hostID="+str(h['hostid']))
			count=count+1

	print("\nTotal number of Zabbix Agent registered with Server = "+str(total)+"\nTotal number of offline Zabbix Agent = "+str(count))

if __name__ == "__main__":
	get_offline_zabbix_host()
