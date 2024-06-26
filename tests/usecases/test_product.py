async def test_usecases_should_return_sucess():
    result = await usecase.create()

    assert isinstance(result, ProductOut)