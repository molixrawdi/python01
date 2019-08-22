# vagrant init ubuntu/bionic64
Vagrant.configure("2") do |config|

   config.vm.provider "virtualbox" do |vb|
    vb.memory = 1024
    vb.cpus = 2
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]

  end
  config.vm.define "python01" do |subconfig|
    subconfig.vm.box = "hashicorp/bionic64"
    subconfig.vm.hostname = "python01"
    subconfig.vm.network :private_network, ip: "10.0.0.13"
    subconfig.vm.provision "shell", inline: <<-SHELLMASTER
      sudo apt -y update
      sudo apt-get -y install gcc make
      sudo apt -y install software-properties-common
      sudo apt-get -y install python3-venv
      sudo apt install -y zlib1g-dev libffi-dev build-essential libssl-dev libffi-dev python-dev
      sudo apt upgrade -y python3
      sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
    SHELLMASTER
  end
end