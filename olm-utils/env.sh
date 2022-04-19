#!/bin/sh
SERVER=

# Username and password
KUBEADMIN_USER=
KUBEADMIN_PASS=
# OR
# APITOKEN
API_TOKEN=


# SCRIPT
#Pod login and auto login to oc cluster from runutils
if  [ -n "$KUBEADMIN_USER" ] && [ -n "$KUBEADMIN_PASS" ]
    then
        alias oclogin_auto="run_utils login-to-ocp -u ${KUBEADMIN_USER} -p ${KUBEADMIN_PASS} --server=${SERVER}";
        alias pod_login="oc login -u ${KUBEADMIN_USER} -p ${KUBEADMIN_PASS} --server ${SERVER}";
    else
        if  [ -z "$API_TOKEN" ]
            then
                    exit 1;
            else
                alias pod_login="oc login --token=${API_TOKEN} --server=${SERVER}";
                alias oclogin_auto="run_utils login-to-ocp --token=${API_TOKEN} --server=${SERVER}";
        fi
fi
# Pod login
pod_login

# Check if the last command executed properly
if [ $? -eq 0 ]; then
    echo "Logged in Successfully";
else
    echo "Login Failed";
    exit 1;
fi


# Deploy olm_utils to cluster
export PROJECT_NAME='olm-utils'
oc create namespace ${PROJECT_NAME}
oc project ${PROJECT_NAME}
oc apply -f deployment.yaml

# # Setting the aliases
alias run_utils="kubectl exec ${PROJECT_NAME} --";
alias oclogin="run_utils login-to-ocp";
alias get_pods="kubectl get pods -n $PROJECT_NAME";
# alias oclogin_auto="run_utils login-to-ocp --token=${API_TOKEN} --server=${SERVER}"
alias get_preview="kubectl cp $PROJECT_NAME/$PROJECT_NAME:/tmp/work/preview.sh ${CHE_PROJECTS_ROOT}/techzone-demo/olm-utils/preview.sh"

