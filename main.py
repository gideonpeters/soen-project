import understand
import sys

def projectMetrics(db):
  # get just the metrics we need rather than all metrics
  # this started to occasionally hang on scitools build 651
  # metrics = db.metric(db.metrics())

  countLine = 0
  countLineCode = 0
  sumCyclomatic = 0

  for func in db.ents("file"):
    metric = func.metric(("CountLine","CountLineCode","SumCyclomatic"))
    if metric["CountLine"] is not None:
      countLine += metric["CountLine"]
    if metric["CountLineCode"] is not None:
      countLineCode += metric["CountLineCode"]
    if metric["SumCyclomatic"] is not None:
      sumCyclomatic += metric["SumCyclomatic"]

  print("SumCyclomatic,CountLine,CountLineCode")
  print(sumCyclomatic,",",countLine,",",countLineCode)


if __name__ == '__main__':
#   args = sys.argv
  db = understand.open("understand-experiments.und")
  projectMetrics(db)
#   for func in db.ents("function,method,procedure"):
#     file = "callby_" + func.name() + ".png"
#     print (func.longname(),"->",file)
    # func.draw("Called By",file)


  
# def check(check, file):
#     """
#     The check overload for a non-project level check.
#     """
#     for ref in file.filerefs('define', 'function'):
#         # Use is_aborted to see if an abort was requested
#         if check.is_aborted():
#             return

#         ent = ref.ent()
#         if ent.name() == 'main':
#             # Store the violation returned from check.violation to add
#             # more details
#             violation = check.violation(ent, file, ref.line(), ref.column(),
#                                         'definition of %1 function', ent)
#             # You can add fix it hints to violations
#             violation.add_fixit_hint(ref.line(), ref.column(), ref.line(),
#                                      ref.column() + len(ent.name()), 'foo')