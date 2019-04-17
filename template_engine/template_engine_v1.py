
text = '<p>Topics for {{name}}</p>'
context  = {'name':'owen'}

class Templite(object):
    def __init__(self,text,context):
        text = text
        self.context = context

        import re
        tokens = re.split(r'({{.*?}})',text)


        code = []

        code.extend(['def render_context(context):','\n'," "*4])
       
        code.extend(['result = []','\n',' '*4])
 

        for token in tokens:
            if token.startswith('{{'):
                token = token[2:-2]
                code.extend(['%s =  context["%s"]'%(token,token),'\n',' '*4])
                code.extend(['result.append(%s)'%(token),'\n',' '*4])
            else:
                code.extend(['result.append("%s")'%(token),'\n',' '*4])


        code.append('return "".join(result)')
        code = ' '.join(code)
        print (code)

        global_namespace = {}
        exec(code,global_namespace)
        self.render_context = global_namespace['render_context']
    
    def render(self):
        return self.render_context(self.context)


tem = Templite(text,context)
print(tem.render())
