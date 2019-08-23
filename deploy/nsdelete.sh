#!/bin/bash

# set variable by querying k8s for a namespace named tomster, return line for tomster, print first field
tomster=$(kubectl get ns | awk '/tomster/ {print $1}')

# check if tomster variable is nonzero
if [ -n "$tomster" ]

# if true, as in the variable is nonzero, as in the awk returned something
then
  echo "tomster namespace found"
  kubectl delete ns tomster > /dev/null 2>&1
  while [ -n "$tomster" ]
    do
      tomster=$(kubectl get ns | awk '/tomster/ {print $1}')
      echo "tomster namespace deleting"
      sleep 5
    done
    echo "tomster namespace deleted"

# if not true, as in the variable is zero, as in the awk returned null
else
  echo "tomster namespace not found, nothing to delete"
  
# end if  
fi
