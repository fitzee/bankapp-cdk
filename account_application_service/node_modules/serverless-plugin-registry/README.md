Serverless Registry Plugin 
==========================
[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
[![npm version](https://badge.fury.io/js/serverless-plugin-registry.svg)](https://badge.fury.io/js/serverless-plugin-registry)
[![npm downloads](https://img.shields.io/npm/dm/serverless-plugin-registry.svg)](https://www.npmjs.com/package/serverless-plugin-registry)
[![license](https://img.shields.io/npm/l/serverless-plugin-registry.svg)](https://raw.githubusercontent.com/aronim/serverless-plugin-registry/master/LICENSE)

Register function names with AWS SSM Parameter Store

**Requirements:**
* Serverless *v1.12.x* or higher.
* AWS provider

### How it works

This plugin creates an SSM Parameter with your functions' fully qualified Lambda Function names as values. The main 
motivation for this plugin is to remove the dependency that any client code would have on the AWS Stack, as the stack 
name is part of the fully qualified Lambda Function name. Using this plugin, it is easier to move functions between 
stacks with out less changes to client code and configuration.

### Caveats

One caveat is the fact that any IAM policies that are written for these functions will still need to be updated. In the 
case of Serverless configuration, if you use the built-in SSM Parameter resolution, then it might be as simple as just 
redeploying any client upstream services.


### Setup

 Install via npm in the root of your Serverless service:
```
npm install serverless-plugin-registry --save-dev
```

* Add the plugin to the `plugins` array in your Serverless `serverless.yml`:

```yml
plugins:
  - serverless-plugin-registry
```

### Default Behavior

```yml
service: ServerlessPluginRegistry

provider:
  stage: ${opt:stage, "Test"}

functions:
  Hello:
    handler: hello.js
```

This will produce an SSM Parameter with 
- Name: /ServerlessPluginRegistry/Test/Hello
- Value: ServerlessPluginRegistry-Test-Hello

### Global Base Name

```yml
service: ServerlessPluginRegistry

provider:
  stage: ${opt:stage, "Test"}

custom:
  registry:
    baseName: /Registry/${self:provider.stage}

functions:
  Hello:
    handler: hello.js
```

This will produce an SSM Parameter with 
- Name: /Registry/Test/Hello
- Value: ServerlessPluginRegistry-Test-Hello

### Function Base Name

```yml
service: ServerlessPluginRegistry

provider:
  stage: ${opt:stage, "Test"}

functions:
  Hello:
    handler: hello.js    
    registry:
      baseName: /Registry/${self:provider.stage}
```

This will produce an SSM Parameter with 
- Name: /Registry/Test/Hello
- Value: ServerlessPluginRegistry-Test-Hello

### Only Publish Select Functions

```yml
service: ServerlessPluginRegistry

provider:
  stage: ${opt:stage, "Test"}

functions:
  Hello:
    handler: hello.js    
    registry:
      baseName: /Registry/${self:provider.stage}
  HowAreYou:
    handler: howAreYou.js    
    registry:
      register: true
  Goodbye:
    handler: goodbye.js    
```

This will only produce two SSM Parameters with
 
- Name: /Registry/Test/Hello
- Value: ServerlessPluginRegistry-Test-Hello

- Name: /ServerlessPluginRegistry/Test/HowAreYou
- Value: ServerlessPluginRegistry-Test-HowAreYou

## Contribute

Help us making this plugin better and future proof.

* Clone the code
* Install the dependencies with `npm install`
* Create a feature branch `git checkout -b new_feature`
* Lint with standard `npm run lint`

## License

This software is released under the MIT license. See [the license file](LICENSE) for more details.
