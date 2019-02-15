while read IPADDR
do 
    sudo ufw deny from "$IPADDR"
done < iplist.txt
