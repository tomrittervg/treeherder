web: newrelic-admin run-program gunicorn treeherder.config.wsgi:application --timeout 20
worker_beat: newrelic-admin run-program celery beat -A treeherder
worker_pushlog: newrelic-admin run-program celery worker -A treeherder --without-gossip --without-mingle --without-heartbeat -Q pushlog --concurrency=5
worker_store_pulse_jobs: newrelic-admin run-program celery worker -A treeherder --without-gossip --without-mingle --without-heartbeat -Q store_pulse_jobs --concurrency=3
worker_store_pulse_resultsets: newrelic-admin run-program celery worker -A treeherder --without-gossip --without-mingle --without-heartbeat -Q store_pulse_resultsets --concurrency=3
worker_read_pulse_jobs: newrelic-admin run-program ./manage.py read_pulse_jobs
worker_read_pulse_pushes: newrelic-admin run-program ./manage.py read_pulse_pushes
worker_default: newrelic-admin run-program celery worker -A treeherder --without-gossip --without-mingle --without-heartbeat -Q default,generate_perf_alerts,seta_analyze_failures --concurrency=3
worker_log_parser: newrelic-admin run-program celery worker -A treeherder --without-gossip --without-mingle --without-heartbeat -Q log_parser,log_parser_fail,log_store_failure_lines,log_store_failure_lines_fail,log_crossreference_error_lines,log_crossreference_error_lines_fail,log_autoclassify,log_autoclassify_fail --maxtasksperchild=50 --concurrency=7

release: ./bin/pre_deploy
