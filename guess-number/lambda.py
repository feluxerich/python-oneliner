# (lambda: (
#     r := __import__('random').randint(1, 100),
#     print(r),
#     (
#         f := lambda: (
#             i := int(input()),
#             (
#                 print('zu klein'),
#                 f()
#             ) if i < r else (
#                 print('zu groß'),
#                 f()
#             ) if i > r else print('richtig')
#         )
#     )()
# ))()

(lambda:(r:=__import__('random').randint(1,100),(f:=lambda:(i:=int(input()),(print('zu klein'),f())if i<r else(print('zu groß'),f())if i>r else print('richtig')))()))()