Fosbury Python Client
==================

A Python Client for Fosbury (http://fosbury.co). Fosbury is a platform to create Passbook templates, campaigns and passes.

Wraps around the Fosbury API. See the documentation at [Apiary.io](http://docs.fosbury.apiary.io/).

# Installation

The Python library comes as a PyPi gem (see [Fosbury Python Client at PyPi](https://pypi.python.org/fosbury/fosbury/0.9.1) )

Install the gem by issuing

```python
pip install fosbury
```

and require it in your project

```python
import fosbury
```

Happy passing!

# Usage

## Authorization

To authorize, set the API key. Please send a mail to api@fosbury.co to obtain the API key of your Fosbury account. 

```python
client = fosbury.Client(api_token='[your_api_token]')
```

## Generating campaigns

In order to generate passes, you need to generate a template (a pass layout) and a campaign (a collection of passes). For more information on parameters and options, see the [API Documentation](http://docs.fosbury.apiary.io/)

```python
# Basic coupon campaign generation example
# Create a basic template
# Initialize the API client
campaign = client.create_template('My template', 'coupon', {'primary_label': '20%', 'primary_value': 'Discount'})

# Create a campaign with 10 passes
# Because the barcode_type is set to 'single', 
# only one pass will be rendered that can be installed 10 times.
campaign = client.create_campaign(template['id'],
                                   {'quantity': 10,
                                    'barcode': '12345',
                                    'barcode_type': 'single'}
                                   )

# Distribute the campaign, the pass will be rendered.
# The returned JSON provides information about the generic url to download passes.
client.distribute_campaign(campaign['id'])
```

## Generating single passes

When generating seperate passes, create a template and campaign first. After that, passes can be created with the createPass function. For more information on parameters and options, see the [API Documentation](http://docs.fosbury.apiary.io/)

```python
# Create a basic template
template = create_template('My template',
                           'coupon',
                           {'primary_label':'20%',
                            'primary_value':'Discount'}
                           )

# Create a campaign with quantity 1 (more passes can be created later)
# Barcode is ommited, this will provided on pass creation level
campaign = client.create_campaign(template['id'], {'quantity':1})

# Create a backfield for the pass
client.create_campaign_backfield(campaign['id'],
                                  'Backfield title',
                                  'Backfield description')

# Add a geofenced location to the pass
client.create_campaign_location(campaign['id'],
                                 54.33,
                                 4.44,
                                 'Starbucks Coffee')

# Distribute the campaign to make it public and render the first pass
client.distribute_campaign(campaign['id'])

# Create 2 passes with the campaign above.
# The returned JSON contains information on the location of the .pkpass files.
pass1 = client.create_pass(campaign,
                            {'barcode':'11111',
                             'secondary_label':'John',
                             'secondary_label':'Doe'}
                            )

pass2 = client.create_pass(campaign,
                            {'barcode':'22222',
                             'secondary_label':'Jane',
                             'secondary_label':'Doe'}
                            )
```
## Pushing updates

**Note**: A pass holder will only receive a push update if one of the field values is changed. For more information about field names, take a look at our [API Documentation](http://docs.fosbury.apiary.io/).

Fosbury allows push notifications to be sent to passes. To achieve this, first update a pass and send a push notification afterwards. 

```python
// Update a pass. 
// Note: the updatePass accepts a pass serial number or an id as identifier.
client.update_pass('FSBABC123', {'secondary_value': '50% off!'})

// Send the push notification to the pass
client.push_pass('FSBABC123', {'secondary_changed_message': '50% off!'})
```