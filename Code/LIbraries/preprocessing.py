



def RemoveTextCookie(df):
  text_cookie="portale utilizza cookie tecnici"
  for i in range(len(df['Testo'])):

    if text_cookie in str(df['Testo'][i]):
      df=df.drop(i)

  return df.reset_index(inplace=True)

  