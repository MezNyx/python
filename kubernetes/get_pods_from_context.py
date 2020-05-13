#!/usr/bin/env python3

from kubernetes import client, config
from pick import pick

def main():
  contexts, active_context = config.list_kube_config_contexts()
  if not contexts:
    print("Cannot find any context in kube-config file.")
  contexts = [context['name'] for context in contexts]
  active_index = contexts.index(active_context['name'])
  option, _ = pick(contexts, title="Pick the context to load",
                   default_index=active_index)
  config.load_kube_config(context=option)
  v1 = client.CoreV1Api()
  namespaces = v1.list_namespace(watch=False)
  print(namespaces)
"""
  pod_list = v1.list_namespaced_pod(namespace)
  for pod in pod_list.items:
    print("%s\t%s\t%s" % (pod.metadata.name, pod.status.phase, pod.status.pod_ip))
"""


main()
