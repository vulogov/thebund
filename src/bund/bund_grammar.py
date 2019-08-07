bund_grammar="""
BundContexts:
  history*=HistoryElement?
  env*=EnvironmentElement?
  contexts*=Context?
;

HistoryElement:
  '[history'
    story*=HistoryElementKV
  ';;'
;

HistoryElementKV:
  name=ID 'is' he_val=BASETYPE
;

EnvironmentElement:
  '[env'
    envstatement += EnvStatement
  ';;'
;

EnvStatement:
  name=ID "is" type=ID("[" param=BASETYPE "]")?
;

Context:
  name=ID 'is'
    statements+=Statement
  ';;'
;

Statement:
  DataBlock | CodeBlockDecl | InBlockDecl | OutBlockDecl | VarBlockDecl
;

DataBlock:
  '[data'
    definitions+=DataDefinitions[/,|;|(\s)*|(\n)*/]
    codeblock=CodeBlock?
  ';;'
;

CodeBlockDecl:
  name=ID 'is' codeblock=CodeBlock
;

InBlockDecl:
  '[in'
    in_chan += ChannelDefs
  ';;'
;

OutBlockDecl:
  '[out'
    out_chan += ChannelDefs
  ';;'
;

ChannelDefs:
  name=ID "is" type=ChannelType
    attrs *= ChannelAttrs[/,|;|(\s)*|(\n)*/]
  ";;"
;

ChannelType:
  "file" | "pipe"
;

ChannelAttrs:
  name=ID '<-' val=BASETYPE
;

VarBlockDecl:
  '[var'
    PushAssignment | PullAssignment
  ';;'
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
  "(" words+=CodeWords ")"
;

CodeBlockRef:
  /'|&/"(" words+=CodeWords ")"
;

CodeWords:
  Data | CodeWord | CodeWordWRef | CodeWordSpecial | CodeBlock | CodeBlockRef
;

CodeWordModifyer:
  '+' | '-' | '*' | '&' | '=' | '?' | '!' | '$' | '@' | '%' | '^'
;

CodeWordSpecial:
  '++' | '--' | '==' | '<=' | '=>' | '<' | '>' | '===' | '+++' | '---'
;

CodeWordRef:
  '::' | '->' | '<-'
;

CodeWord:
  prefix=CodeWordModifyer? word=ID? suffix=CodeWordModifyer? param=CurryParam?
;

CodeWordWRef:
  ':' base=ID CodeWordRef word=ID
;

CurryParam:
  "@" param=Data
;

Comment:
  /\/\*.*\*\/|\/\/.*$/
;
"""
