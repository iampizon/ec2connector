import os
import sys
import boto3

#########CONFIG############################
key_path = "/Users/Your/Documents"
###########################################

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

#build connections
connections = dict()
for v in response["Reservations"]:
	for instance in v["Instances"]:
#		print(instance)
		if not instance["State"]["Name"] == "running":
			continue

		key_name = "N/A"
		if "KeyName" in instance:
			key_name = instance["KeyName"] + ".pem"

		tag_name = "#Noname"	
		for tag in instance["Tags"]:
			if tag["Key"] == "Name" and len(tag["Value"]) > 0:
				tag_name = tag["Value"]
		
		public_ip = "N/A"
		for nic in instance["NetworkInterfaces"]:
			if "Association" in nic:
				public_ip = nic["Association"]["PublicIp"]

		connections[tag_name] = {"id":instance["InstanceId"], 
			"ip":public_ip, 
			"key":key_name, 
			"name":tag_name, 
			"type":instance["InstanceType"]}

#sort and show
index = 1
print("---------------------------------------------------------------------------------------------------------")
for k,v in sorted(connections.items()):
	instance_info = v["name"] + " (" + v["id"] + ")"
	print(str(index).rjust(3) 
			+ "|" + instance_info.ljust(50) 
			+ "|" + v["type"].ljust(15) 
			+ "|" + v["ip"].ljust(16) 
			+ "|" + v["key"])

	v["index"] = index
	connections[k] = v
	index = index + 1

#input and run
while(1):
	select = input(" ?> " )
	if select == "x":
		sys.exit()

	if not select.isdigit():
		print("select number to connect, press x to exit.")
		continue

	for v in connections.values():
		if not str(v["index"]) == str(select):
			continue

		command = "ssh -i " + key_path + "/" + v["key"] + " ec2-user@" + v["ip"]
		print("running... " + command)
		os.system(command)
		sys.exit()


