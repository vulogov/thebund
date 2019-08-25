bund_grammar="""
BundContexts:
  history*=HistoryElement?
  env*=EnvironmentElement?
  contexts*=Context?
;

HistoryElement:
  '[history'
    story+=HistoryElementKV[/,|;|(\s)*|(\n)*/]
  ';;'
;

HistoryElementKV:
  name=ID 'is' he_val=BASETYPE
;

EnvironmentElement:
  '[env'
    envstatement += EnvStatement[/,|;|(\s)*|(\n)*/]
  ';;'
;

EnvStatement:
  name=/\w+(\.\w+)*/ "is" type=EnvStatementType("[" param=BASETYPE "]")? ("as" real_name=ID)?
;

EnvStatementType:
  "module" | "python" | "log"
;

Context:
  name=ID 'is'
    statements*=Statement
  ';;'
;

Statement:
  DataBlock | CodeBlockDecl | CodeBlockMonadDecl | InBlockDecl | OutBlockDecl | VarBlock
;

DataBlock:
  '[data'
    definitions+=DataDefinitions[/,|;|(\s)*|(\n)*/]
    codeblock=CodeBlock?
  ';;'
;

VarBlock:
  '[var'
    definitions+=DataDefinitions[/,|;|(\s)*|(\n)*/]
  ';;'
;

ArityDecl:
  "|" a+=ArityElement[/,|;|(\s)*|(\n)*/] "|"
;

ArityElement:
  "_" | "str" | "int" | "float" | "list" | "dict" | "code"
;

CodeBlockDecl:
  name=ID 'is' codeblock=CodeBlock
;

CodeBlockMonadDecl:
  name=ID  arity=ArityDecl? 'is' codeblock=CodeWordsMonad
;

InBlockDecl:
  '[in'
    in_chan += ChannelDefs[/,|;|(\s)*|(\n)*/]
  ';;'
;

OutBlockDecl:
  '[out'
    out_chan += ChannelDefs[/,|;|(\s)*|(\n)*/]
  ';;'
;

ChannelDefs:
  btype=ChannelBlockType? name=ChannelName("[" attr=Data "]")? "is" type=ChannelType ("as" ch_name=ID)?
;

ChannelType:
  "file" | "tmpfile" | "pipe" | "list" | "queue" | "string"
;

ChannelBlockType:
  "block" | "text"
;

ChannelName:
  ID | STRING
;

ChannelAttrs:
  name=ID '<-' val=BASETYPE
;

DataDefinitions:
  PushAssignment | PullAssignment
;

PushAssignment:
  value=Data '->' name=ID
;

PullAssignment:
  name=ID '<-' value=Data
;

List:
  '[' value+=Data[','] ']'
;

KVData:
  name=ID '<-' value=Data
;

KV:
  '{' kvalue+=KVData[',']
  '}'
;

Data:
  BASETYPE | List | KV | CodeBlock | CodeBlockRef
;

CodeBlock:
  arity=ArityDecl? "(" words+=CodeWords ")"
;

CodeBlockRef:
  arity=ArityDecl? "&(" words+=CodeWords ")"
;

CodeWords:
  Data | CodeWord | CodeWordWReferenceOnModule | CodeWordSpecial | CodeWordModifyer | CodeBlock | CodeBlockRef |  CodeExecute | CodeWordLazy | CodeLazyEval | CodeWordsMonad
;

CodeWordModifyer:
  '+' | '-' | '*' | '&' | '=' | '?' | '!' | '$' | '@' | '%' | '^' | '|'
;

CodeWordSpecial:
  '++' | '--' | '==' | '<=' | '=>' | '<' | '>' | '===' | '+++' | '---'
;

CodeWordReferenceOnModule:
    '->'
;


CodeWord:
  prefix=CodeWordModifyer? word=ID suffix=CodeWordModifyer? param=CurryParam?
;

CodeWordNoParam:
  prefix=CodeWordModifyer? word=ID suffix=CodeWordModifyer?
;

CodeWordWReferenceOnModule:
  ":"module=ID CodeWordReferenceOnModule fun=ID
;


CurryParam:
  "@" param=Data
;

CodeWordLazy:
  ":" word=CodeWordMonad
;

CodeWordsMonad:
  arity=ArityDecl? "#("
     words += CodeWordMonad
  ")" param=CurryParam?
;

CodeWordMonad:
  CodeWordNoParam | CodeWordSpecial | CodeWordModifyer | CodeWordWReferenceOnModule
;

CodeExecute:
  "." name=ID?
;

CodeLazyEval:
  ";" name=ID?
 ;

Comment:
  /\/\*.*\*\/|\/\/.*$|^\#.*$/
;
"""
