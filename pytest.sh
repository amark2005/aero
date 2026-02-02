echo "Running "
if ! dnf list --installed | grep -i python3-numpy python3-matplotlib python3-qt &> /dev/null; then
    echo ""
else
    sudo dnf5 install python3-numpy
    sudo dnf5 install python3-matplotlib
    sudo dnf5 install python3-qt5
    fi

python3 bernouli-theorem.py
echo "Randi"