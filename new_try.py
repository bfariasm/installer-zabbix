#!/usr/bin/python3
import os
import shutil
import mysql.connector

class Zabbix:

    def __init__(self):
        pass

    def menu(self):
        os.system('clear')

        print('''\nEscolha uma opção
        [1] Instalar Dependências
        [2] Zabbix
        [3] Sair             
        ''')

        self.choice = int(input())

        if self.choice == 1:
            Zabbix.install_apt(self)
        elif self.choice == 2:
            Zabbix.ver_zbx(self)

    def ver_zbx(self):
        os.system('clear')

        print('''Qual versão do Zabbix deseja instalar?
        [1] 4.0.x
        [2] 4.4.x
        [3] 5.0.x
        [4] Voltar ao menu.


        TODA A INSTAÇÃO SERÁ FEITA NA PASTA OPT
        ''')

        self.menu_ver = int(input())

        if self.menu_ver == 1:
            Zabbix.install_zbx(self,'4.0.20','4,0', 'frontends/php')
        elif self.menu_ver == 2:
            Zabbix.install_zbx(self,'4.4.8','4.4', 'frontends/php')
        elif self.menu_ver == 3:
            Zabbix.install_zbx(self,'5.0.0','5.0', 'ui')            

    def install_apt(self):
        os.system('apt update -y && apt upgrade -y && apt autoremove')
        os.system('apt-get update -y && apt-get upgrade -y && apt-get autoremove')
        os.system('''apt-get -y install mysql-server apache2 software-properties-common snmp checkinstall libevent-rpc-perl libhttp-daemon-ssl-perl 
            libio-socket-ssl-perl libnet-imap-simple-perl libnet-smtp-ssl-perl libapt-pkg-perl libnet-ssleay-perl libauthen-pam-perl libio-pty-perl 
            apt-show-versions nmap tcpdump ntpdate build-essential fping libsnmp-dev libcurl4-openssl-dev libiodbc2-dev libapache2-mod-php php-gd 
            libiksemel-dev libssh2-1-dev gammu openipmi libopenipmi-dev libmysqlclient-dev htop ncftp language-pack-pt-base rcconf 
            traceroute libxml2-dev libevent-dev libpcre3-dev libbz2-dev mariadb-server-10.3''')
        #os.system('apt install python3-pip')
        os.system('pip3 install --upgrade pip')
        os.system('pip3 install MySQL-python')
        #os.system('pip3 install mysql-connector-python')
        os.system('pip3 install pymysql')

        os.system('clear')

        print('''\n Deseja instalar as dependências do PHP? (Recomendado!)
        [1] Sim
        [2] Volta ao menu.

        ''')

        self.php_choice = int(input())
        if self.php_choice == 1:
            Zabbix.apt_php(self)
        elif self.php_choice == 2:
            Zabbix.menu(self)

    def install_zbx(self, version, url, loc_php):
        self.version = version
        self.url = url
        self.loc_php = loc_php
        '''
        os.system('groupadd zabbix')
        os.system('useradd zabbix -g zabbix')
        os.mkdir('/opt/zabbix/')
        os.chdir('/tmp/')
        os.system('wget https://cdn.zabbix.com/zabbix/sources/stable/%s/zabbix-%s.tar.gz'%(self.url, self.version))
        os.system('tar -zxvf zabbix-%s.tar.gz'%(self.version))
        os.system('mv zabbix-%s /opt/zabbix/'%(self.version))
        os.chdir('/opt/zabbix/zabbix-%s'%(self.version))
        os.system('./configure --enable-server --enable-agent --with-mysql --with-net-snmp --with-libcurl --with-openipmi --with-ssh2 --with-iodbc --with-libxml2 --enable-ipv6')       
        os.system('make install')
        os.system('cp -r misc/init.d/debian/* /etc/init.d/')
        os.system('chmod 755 /etc/init.d/zabbix-server')
        os.system('update-rc.d zabbix-server defaults')
        os.system('chmod 755 /etc/init.d/zabbix-agent')
        os.system('update-rc.d zabbix-agent defaults')
        os.system('chown root:zabbix /usr/bin/fping')
        os.system('chmod 710 /usr/bin/fping')
        os.system('chmod ug+s /usr/bin/fping')
        os.system('ln -s /usr/bin/fping /usr/sbin/fping')
        os.system('ln -s /usr/bin/fping6 /usr/sbin/fping6')
        os.mkdir('/var/www/html/zabbix/')
        os.chdir('%s'%(self.loc_php))
        os.system('cp -a . /var/www/html/zabbix')
        os.system('/etc/init.d/zabbix-agent start')
        os.system('/etc/init.d/zabbix-server start')
        os.system('/etc/init.d/apache2 start')
        '''
        Zabbix.zbx_sql(self, self.version)
        
    def zbx_sql(self, sql_dir):
        self.sql_dir = sql_dir
        
        print('Digite a senha do banco de dados: ')
        self.pass_db = input()
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd=self.pass_db
            )
        mycursor = mydb.cursor()
        mycursor.execute('CREATE DATABASE zabbix character set utf8 collate utf8_bin')


    def exit(self):
        os.system('exit')

    def apt_php(self):
        os.system('clear')
        os.system('add-apt-repository -y ppa:ondrej/php')
        os.system('apt update -y && apt upgrade -y && apt autoremove')
        os.system('apt-get update -y && apt-get upgrade -y && apt-get autoremove')
        os.system('''apt-get install -y php7.0 php5.6 php5.6-mysql php-gettext php5.6-mbstring php-mbstring php7.0-mbstring php-xdebug 
            libapache2-mod-php5.6 libapache2-mod-php7.0 php7.0-xml php7.0-xmlwriter php7.0-bcmath php7.4 php7.4 php7.4-mysql php7.4-gettext 
            php7.4-mbstring php7.4-xdebug libapache2-mod-php7.4 libapache2-mod-php7.4 php7.4-xml php7.4-xmlwriter php7.4-bcmath php-bcmath''')
        Zabbix.menu(self)


zbx = Zabbix()
zbx.menu()
