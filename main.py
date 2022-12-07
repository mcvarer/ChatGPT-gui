import openai


class OpenapiOPS():

    def __int__(self, api_key):
         self.api_key = api_key

    def chat_prompt(self, message: str) -> str:
        """

        :param message:
        :return:
        """
        openai.api_key = self.api_key
        chatgpt = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message,
            max_tokens=1024,
            temperature=0.5,
            n=1,
            stop=None
        )
        return chatgpt["choices"][0]["text"]
