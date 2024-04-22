# 2-execute_a_command.pp

exec { 'kill':
  command     => 'pkill -f killmenow',
  refreshonly => true, # This ensures the command is only executed if a resource notifies it.
}

notify { 'Command executed successfully':
  subscribe => Exec['kill'], # This notifies the 'notify' resource when the 'exec' resource is executed successfully.
}

g