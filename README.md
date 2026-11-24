# alfajr_alarm_with_flutter
An example hook script to check the commit log message.
Called by "git commit" with one argument, the name of the file
that has the commit message. The hook should exit with non-zero
status after issuing an appropriate message if it wants to stop the
commit. The hook is allowed to edit the commit message file.

HOOK_FILE=$1
COMMIT_MSG=`head -n1 $HOOK_FILE`
# PATTERN="^[A-Z][A-Z0-9]+-[0-9]+"
PATTERN="^AAUF+-[0-9]+"
if [[ ! ${COMMIT_MSG} =~ $PATTERN ]]; then
  echo ""
  echo "    ERROR! Bad commit message. "
  echo "    '$COMMIT_MSG' is missing JIRA Ticket Number."
  echo "    example: 'AAUF-1234: my commit'"
  echo ""
  exit 1
fi