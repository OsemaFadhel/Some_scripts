#! bin/bash

#		::::::::::           :::        :::::::::       :::::::::       ::::::::::       :::
#		:+:                :+: :+:           :+:             :+:        :+:              :+:
#		+:+               +:+   +:+         +:+             +:+         +:+              +:+
#	:#::+::#         +#++:++#++:       +#+             +#+          +#++:++#         +#+
#	+#+              +#+     +#+      +#+             +#+           +#+              +#+
#	#+#              #+#     #+#     #+#             #+#            #+#              #+#
#	###              ###     ###    #########       #########       ##########       ##########


echo "Installing Norminette"

if ! command -v python3 &> /dev/null
then
	echo "Python3 could not be found"
	echo "Please install python3"
	exit
fi

//see if norminette is already installed

if command -v norminette &> /dev/null
then
	echo "Norminette is already installed"

	echo "Updating Norminette"
	python3 -m pip install --upgrade norminette
	echo "Norminette updated"
	exit
fi

//install norminette

python3 -m pip install --upgrade pip setuptools

python3 -m pip install norminette

